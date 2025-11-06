from app.utils import handle_page
from sqlalchemy import desc
from app import db


class BaseService:
    def __init__(self, model):
        self.model = model

    # 添加数据
    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    # 查询单条
    def get(self, id):
        return self.model.query.get(id)

    # 查询所有
    def all(self, filters=None, order_by=None):
        query = self.model.query
        if filters:
            query = query.filter_by(**filters)
        if order_by:
            query = query.order_by(order_by)

        return query.all()

    # 分页查询
    def paginate(
        self, page=1, per_page=10, filters=None, order_by=None, desc_order=False
    ):
        query = self.model.query
        if filters:
            query = query.filter_by(**filters)
        if order_by:
            order_col = getattr(self.model, order_by)
            if desc_order:
                query = query.order_by(desc(order_col))
            else:
                query = query.order_by(order_col)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        counts = handle_page(page, pagination)
        return {
            "items": [item.to_dict() for item in pagination.items],
            "total": pagination.total,
            "page": pagination.page,
            "pages": counts,
            "max_page": pagination.pages,
        }

    # 更新
    def update(self, id, **kwargs):
        instance = self.get(id)
        if not instance:
            return None
        for key, value in kwargs.items():
            setattr(instance, key, value)
        db.session.commit()

        return instance

    # 删除
    def delete(self, id, soft=True):
        instance = self.get(id)
        if not instance:
            return None
        if soft and hasattr(instance, "deleted_at"):
            from time import time

            instance.deleted_at = int(time())
        else:
            db.session.delete(instance)
        db.session.commit()

        return instance
