# -*- coding: utf-8 -*-
from pushbullet import PushBullet

pb = PushBullet('F8WuT1U8GMYCSRXxyJSQewC84j4SoD8X')

success, push = pb.push_note("NDM CP장애 발생!", "호수 대량 삭제 발생함!!")