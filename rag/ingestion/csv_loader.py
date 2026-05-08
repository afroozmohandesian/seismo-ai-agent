import pandas as pd

from rag.ingestion.base_loader import BaseLoader


class CSVLoader(BaseLoader):

    def load(self, path: str):

        dataframe = pd.read_csv(path)

        return {
            "type": "csv",
            "rows": dataframe.to_dict(orient="records"),
            "source": path,
        }