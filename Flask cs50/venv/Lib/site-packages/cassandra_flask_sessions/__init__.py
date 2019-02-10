from uuid import uuid4
from datetime import timedelta
import json
from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict
from cassandra.cluster import Cluster


class CassandraSession(CallbackDict, SessionMixin):
    def __init__(self, initial=None, sid=None):
        def on_update(self):
            self.modified = True

        CallbackDict.__init__(self, initial)
        self.sid = sid
        self.modified = False


class CassandraSessionInterface(SessionInterface):
    def __init__(self, cluster=None, port=9042, keyspace='tests'):
        if cluster is None:
            cluster = ['127.0.0.1']
        cluster = Cluster(cluster, port=port)
        self.session = cluster.connect(keyspace)

    def get_cass_expiration_time(self, app, session):
        if session.permanent:
            return app.permanent_session_lifetime
        return timedelta(days=1)

    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            stored_session = self.session.execute('SELECT sid, data FROM sessions WHERE sid=%s', [sid]).current_rows

            if stored_session:
                data = None
                if stored_session[0].data is not None:
                    data = json.loads(stored_session[0].data)
                return CassandraSession(initial=data, sid=stored_session[0].sid)
        sid = self.generate_sid()
        return CassandraSession(sid=sid)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            self.session.execute_async("DELETE FROM sessions WHERE sid=%s", [session.sid])
            if session.modified:
                response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        cass_exp = self.get_cass_expiration_time(app, session)
        cookie_exp = self.get_expiration_time(app, session)
        data = json.dumps(dict(session))

        self.session.execute_async("INSERT INTO sessions (sid, data) VALUES (%s, %s) USING TTL %s",
                                   [session.sid, data, int(cass_exp.total_seconds())])
        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=cookie_exp,
                            httponly=True, domain=domain)
