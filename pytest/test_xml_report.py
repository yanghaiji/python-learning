"""
 pytest -q --junitxml=指定自定义的xml文件 需要运行的nodeids

 nodeids 格式为 test_demo02.py::TestClass::test_one

 本测试执行的语句为
pytest -q --junitxml=junitxml/test_one.xml test_xml_report.py::test_record_xml_attribute
"""


# 在XML报告中为测试用例附加额外的属性信息
def test_record_xml_attribute(record_xml_attribute):
    record_xml_attribute("test_id", 10010)
    record_xml_attribute("classname", "custom_classname")
