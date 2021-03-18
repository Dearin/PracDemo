from WeWorkApi.api.user import User


class TestUser:
    user = User()
    '''
    access_token	是	调用接口凭证。获取方法查看“获取access_token”
    userid	是	成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。
    name	是	成员名称。长度为1~64个utf8字符
    alias	否	成员别名。长度1~32个utf8字符
    mobile	否	手机号码。企业内必须唯一，mobile/email二者不能同时为空
    department	是	成员所属部门id列表,不超过100个
    '''

    def test_001_user_create(self):
        res = self.user.create(userid="test_002_0317", name="zhangSan1", department=[2, 3, 4, 5], mobile='13344445556')
        print(res)
