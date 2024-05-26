from dataclasses import dataclass
from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfigクラスを作成する
# カスタマイズとしてdataclassを使って、frozen=Trueにする
@dataclass(frozen=True)
class BaseConfig:
    SECRET_KEY: str = "SampleSecretKey"
    WTF_CSRF_SECRET_KEY: str = "SampleCSRFSecretKey"

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
