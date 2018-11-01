from datetime import datetime
from .models import Haha, session

class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(
            item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        item['commits'] = int(''.join(item['commits'].split(',')))
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        session.add(Haha(**item))
        return item

    def close_spider(self, spider):
        session.commit()
        session.close()
