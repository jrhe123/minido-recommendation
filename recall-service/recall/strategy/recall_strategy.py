from typing import List

from recall.context import Context


class RecallStrategy:
    def name(self):
        pass

    def recall(self, context: Context, n=20) -> List[int]:
        pass
