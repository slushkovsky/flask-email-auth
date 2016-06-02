class SQLAlchemyMixin(object):
    @classmethod
    def _session(cls):
        raise NotImplementedError('Implement in subclass')

    @classmethod
    def _query(cls):
        return cls._session().query(cls)

    @classmethod
    def _new(cls, *args, **kwargs):
        return cls._add(cls(*args, **kwargs))

    @classmethod
    def _add(cls, instance):
        cls._session().add(instance)
        cls._session().commit()
        return instance

    @classmethod
    def _flush(cls):
        try:
            cls._session().flush()
        except AssertionError:
            if transaction:
                with transaction.manager as manager:
                    manager.commit()
            else:
                cls._session().commit()

    def save(self):
        self._add(self)