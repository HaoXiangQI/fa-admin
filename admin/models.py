# 模型层
from sqlalchemy import Column
from app.database import Base
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TEXT,DATETIME,DECIMAL,TINYINT,CHAR,LONGTEXT


# todo 未添加索引
class Order(Base):
    id = Column(INTEGER(), primary_key=True)
    room_ids = Column(TEXT())
    order_code = Column(VARCHAR(32))
    customer_id = Column(INTEGER())
    buyer_address = Column(VARCHAR(200))
    buyer_phone = Column(VARCHAR(11))
    measure_time = Column(DATETIME())
    install_time = Column(DATETIME())
    expand_area = Column(DECIMAL(6,4))
    projective_area = Column(DECIMAL(6,4),)
    count = Column(TINYINT())
    remark = Column(VARCHAR(300))
    creator = Column(VARCHAR(32))
    create_time = Column(DATETIME())
    update_time = Column(DATETIME())
    delete_time = Column(DATETIME())
    ggid = Column(VARCHAR(8))
    status = Column(TINYINT())
    status_update_time = Column(DATETIME())
    factory_num = Column(VARCHAR(255))
    big_plate_num = Column(INTEGER())
    setting = Column(TEXT())
    customer_name = Column(VARCHAR(255))
    total_price = Column(DECIMAL(8,2))
    received_price = Column(DECIMAL(8,2))
    remaining_price = Column(DECIMAL(8,2))
    is_new_save = Column(TINYINT())
    order_from = Column(TINYINT())

# todo 未添加索引
class Room(Base):
    id = Column(INTEGER(), primary_key=True)
    uid = Column(INTEGER())
    name = Column(VARCHAR(100))
    plank_type = Column(VARCHAR(32))
    type = Column(VARCHAR(32))
    color = Column(TEXT())
    room_area = Column(DECIMAL(6,4))
    expand_area = Column(DECIMAL(6,4))
    projective_area = Column(DECIMAL(6,4))
    style = Column(VARCHAR(32))
    remark = Column(VARCHAR(100))
    json_url = Column(TEXT())
    img_url = Column(VARCHAR(200))
    obj_url = Column(VARCHAR(200))
    mtl_url = Column(VARCHAR(200))
    render_url = Column(VARCHAR(200))
    creator = Column(VARCHAR(32))
    create_time = Column(DATETIME())
    update_time = Column(DATETIME())
    delete_time = Column(DATETIME())
    plate_ids = Column(TEXT())
    forcer_ids = Column(TEXT())
    total_price = Column(DECIMAL(8,2))
    product_status = Column(TINYINT())
    door_ids = Column(TEXT())
    pic_url = Column(VARCHAR(255))
    substrate = Column(VARCHAR(255))
    parts = Column(TEXT())
    lock_new = Column(TINYINT())
    lock = Column(TINYINT())
    lock_password = Column(CHAR(4))
    bPSpecArr = Column(VARCHAR(255))
    compSpecArr = Column(VARCHAR(255))
    big_plank_count = Column(VARCHAR(255))
    other_info = Column(VARCHAR(255))
    color_id = Column(TEXT())
    room_other = Column(TEXT())


# todo 未添加索引
class RoomPlate(Base):
    __tablename__ = 'room_plate'

    id = Column(INTEGER(), primary_key=True)
    room_id = Column(INTEGER())
    type = Column(VARCHAR(50))
    size = Column(VARCHAR(50))
    buyer_address = Column(VARCHAR(200))
    buyer = Column(VARCHAR(255))
    create_time = Column(DATETIME())
    color = Column(VARCHAR(100))
    plate_num = Column(VARCHAR(12))
    ggid = Column(VARCHAR(11))
    uid = Column(INTEGER())
    forcer_mark = Column(VARCHAR(3))
    unique_id = Column(VARCHAR(50))
    plate_name = Column(VARCHAR(20))
    plankId = Column(INTEGER())
    plate_other = Column(LONGTEXT())
    plankNum = Column(VARCHAR(14))








