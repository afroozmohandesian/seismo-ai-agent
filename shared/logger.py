import logging


logging.basicConfig(
    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    ),

    handlers=[
        logging.FileHandler("seismo_ai.log"),
        logging.StreamHandler(),
    ],
)


logger = logging.getLogger(
    "seismo_ai_agent"
)