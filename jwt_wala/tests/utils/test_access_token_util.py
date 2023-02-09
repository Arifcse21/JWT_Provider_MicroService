import jwt
import uuid
import datetime
from dateutil.relativedelta import relativedelta
from jwt_wala.utils import GenerateAccessTokenUtil


def test_access_token_util():
    data = {
        "user_uuid": str(uuid.uuid4()),
        "user_type": "user",
        "iat": datetime.date.today(),
        "exp": datetime.date.today() + relativedelta(days=5, minutes=5)
    }

    a_token = GenerateAccessTokenUtil.access_token_generator(data)
    print(a_token)      # try -rP argument with pytest (pytest -rP)
    assert a_token

