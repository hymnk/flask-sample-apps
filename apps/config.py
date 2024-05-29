from dataclasses import dataclass
from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfigクラスを作成する
# カスタマイズとしてdataclassを使って、frozen=Trueにする
@dataclass(frozen=True)
class BaseConfig:
    SECRET_KEY: str = "SampleSecretKey"
    WTF_CSRF_SECRET_KEY: str = "SampleCSRFSecretKey"
    UPLOAD_FOLDER: str = str(Path(basedir, "apps", "images"))
    LABELS = [
        "unlabeled",
        "person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "street sign",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "hat",
        "backpack",
        "umbrella",
        "shoe",
        "eye glasses",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "plate",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "mirror",
        "dining table",
        "window",
        "desk",
        "toilet",
        "door",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "blender",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush",
    ]

# BaseConfigクラスを継承してLocalConfigクラスを作成する
@dataclass(frozen=True)
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{basedir}/local.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_ECHO: bool = True

@dataclass(frozen=True)
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{basedir}/testing.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    WTF_CSRF_ENABLED: bool = False

# config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
