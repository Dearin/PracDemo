#!/usr/local/bin/python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/14 9:25 PM
# @Author : Deng
# @Site : 
# @File : test_department.py
# @Software : PyCharm
import allure

from WeWorkApi.api.department import Department


class TestDepartmen:
    '''
    todo：
    1-数据清理:思路基于一个节点后去新增对应的测试用例，然后删除这个跟节点一步到位！
    2-安全验证不携带token要怎么测试呢？
    参数说明：
    id		部门id
    name		部门名称。长度限制为1~32个字符，字符不能包括\:?”<>｜
    name_en		英文名称，需要在管理后台开启多语言支持才能生效。长度限制为1~32个字符，字符不能包括\:?”<>｜
    parentid	父部门id
    order	在父部门中的次序值。order值大的排序靠前。有效的值范围是[0, 2^32)
    '''
    department = Department()

    @allure.story("正确名称与父节点id新增部门")
    def test_001_department_create(self):
        res = self.department.create(name='研发中心', name_en='Dev', parentid=1, order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 0
        assert self.department.jsonpath(expr='$..errmsg')[0] == 'created'

    @allure.story("删除部门 - 正确删除节点")
    def test_001_department_delete(self):
        res = self.department.create(name='湖北研发中心', name_en='HBBDev', parentid=2, order=0)
        dept_id = res['id']
        res = self.department.delete(id=dept_id)
        assert self.department.jsonpath('$..errcode')[0] == 0
        assert 'deleted' in self.department.jsonpath('$..errmsg')[0]

    @allure.story("删除部门 - 部门下存在人员")
    def test_001_department_delete_UsersExisted(self):
        res = self.department.delete(id=1)
        assert self.department.jsonpath('$..errcode')[0] == 60005
        assert 'department contains user' in self.department.jsonpath('$..errmsg')[0]

    @allure.story("删除部门 - 部门下存在子部门")
    def test_001_department_delete_ParentDep(self):
        new_dep = self.department.create(name="南京研发中心", parentid=2, order=0)
        p_id = new_dep['id']
        self.department.create(name="南京鼓楼区", parentid=p_id)
        res = self.department.delete(id=p_id)
        assert self.department.jsonpath('$..errcode')[0] == 60006
        assert 'department contains sub-department' in self.department.jsonpath('$..errmsg')[0]

    @allure.story("创建部门时缺少token参数")
    def test_002_department_create(self):
        pass

    @allure.story("部门名称中存在非法字符串")
    def test_003_department_create_wrongName(self):
        res = self.department.create(name='</script>', name_en='WrongName', parentid=2, order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60009
        assert 'department name include invalid char' in self.department.jsonpath(expr='$..errmsg')[0]

    @allure.story("正确名称与不存在的父节点id新增部门")
    def test_004_department_create_parentId_notExist(self):
        res = self.department.create(name='父节点不存在', name_en='NotExist', parentid=1111, order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60004
        assert 'parent department not found' in self.department.jsonpath(expr='$..errmsg')[0]

    @allure.story("添加与父节点同名的部门")
    def test_005_department_create_sameName(self):
        res = self.department.create(name="研发中心", name_en='Dev', parentid=2, order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 0
        assert self.department.jsonpath(expr='$..errmsg')[0] == 'created'

    @allure.story("同一父节点下添加相同名称的子部门")
    def test_006_department_create_sameName(self):
        res = self.department.create(name="研发中心", name_en='Dev', parentid=2, order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60008
        assert 'department existed' in self.department.jsonpath(expr='$..errmsg')[0]

    @allure.story("新增-错误格式父节点id")
    def test_007_department_create_WrongPa(self):
        res = self.department.create(name="父节点格式错误", name_en='WrongFormatPid', parentid='str', order=0)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60009
        assert 'wrong json format' in self.department.jsonpath(expr='$..errmsg')[0]

    @allure.story("根据父节点获取部门详情")
    def test_008_department_list(self):
        '''获取部门列表'''
        res = self.department.list(1)
        assert self.department.jsonpath(expr="$..name")[0] == "Hogwarts"

    @allure.story("修改部门名称")
    def test_009_department_update(self):
        res = self.department.create(name='西安研发中心', name_en='XADev', parentid=2, order=0)
        dep_id = res['id']
        res = self.department.update(name='西安研发中心修改后', id=dep_id, name_en='XaDev', parentid=2, order=0)
        print(res)
        lists = self.department.list(1)
        assert '西安研发中心修改后' in self.department.jsonpath(expr='$..name')

    @allure.story("修改部门-传递不存在的部门id")
    def test_010_department_update_noExistId(self):
        res = self.department.update(id=999, name="noExistId")
        assert self.department.jsonpath(expr='$..errcode')[0] == 60003
        assert 'department not found' in self.department.jsonpath(expr='$..errmsg')[0]

    @allure.story("修改部门-名称中携带非法参数")
    def test_011_department_update_WrongName(self):
        res = self.department.create(name="北京研发中心", parentid=2)
        dept_id = res['id']
        self.department.update(name="<script>", id=dept_id)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60009
        assert 'department name include invalid char' in self.department.jsonpath(expr='errmsg')[0]

    @allure.story("修改部门-修改到不存在的parentid")
    def test_012_department_update_WrongPid(self):
        res = self.department.create(name="新疆研发中心", parentid=2)
        dept_id = res['id']
        res = self.department.update(id=dept_id, parentid=999)
        print(res)
        assert self.department.jsonpath(expr='$..errcode')[0] == 60124
        assert 'invalid parent party id' in self.department.jsonpath(expr='$..errmsg')[0]
