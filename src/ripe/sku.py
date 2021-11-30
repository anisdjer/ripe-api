#!/usr/bin/python
# -*- coding: utf-8 -*-

class SkuAPI(object):

    def list_skus(self):
        url = self.base_url + "skus"
        contents = self.get(url, auth = False)
        return contents

    def get_sku(self, id):
        url = self.base_url + "skus/%d" % id
        contents = self.get(url, auth = False)
        return contents

    def create_sku(self, sku):
        url = self.base_url + "skus"
        contents = self.post(
            url,
            data_j = sku
        )
        return contents

    def update_sku(self, id, sku):
        url = self.base_url + "skus/%d" % id
        contents = self.put(
            url,
            data_j = sku
        )
        return contents

    def delete_sku(self, id):
        url = self.base_url + "skus/%d" % id
        contents = self.delete(url)
        return contents

    def validate_sku(self, id):
        url = self.base_url + "skus/%s/validate" % id
        contents = self.get(url)
        return contents
