from __future__ import annotations

from sqlalchemy.orm import Session

from app.storage.models import TaskGraphModel, TaskNodeModel


class TaskGraphRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_graph(self, graph: TaskGraphModel) -> TaskGraphModel:
        self.db.add(graph)
        self.db.flush()
        return graph

    def create_node(self, node: TaskNodeModel) -> TaskNodeModel:
        self.db.add(node)
        self.db.flush()
        return node

    def list_graph_nodes(self, graph_id: str) -> list[TaskNodeModel]:
        return (
            self.db.query(TaskNodeModel)
            .filter(TaskNodeModel.graph_id == graph_id)
            .order_by(TaskNodeModel.id.asc())
            .all()
        )
