if __name__ == '__main__':
    from fooder.app import create_app
    from fooder.models.base import db_session
    from fooder.models.food import Vegetable
    app = create_app()
    v1 = Vegetable(id='foo', name='potato', description='a root vegetable', category='root')
    db_session.add(v1)
    db_session.commit()
