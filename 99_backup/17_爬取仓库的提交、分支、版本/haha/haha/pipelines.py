from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .models import engine, Git

class HahaPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        item['commits'] = int(item['commits'].replace(',', ''))
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Git(**item))
        return item

    def open_spider(self, spider):
        self.session = sessionmaker(engine)()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
