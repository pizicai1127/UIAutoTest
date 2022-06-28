#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:  2022/6/10 5:49 下午
# @Author: cuiguoen
# @File : test_mall_operation1.py

import pytest
from pages.top.mall_operation1 import SKU_TPU

class TestSKU_TPU:
    # 商城运营菜单下的sku/tpu

    @pytest.mark.p0
    def test_SKU_category(self, topLogin):
        # SPU品类菜单
        page = SKU_TPU(topLogin)
        text_assert = page.SKU_category()
        assert text_assert == "海报 / kv"


    @pytest.mark.p0
    def test_SPU_SKU(self, topLogin):
        # SPU/SKU菜单
        page = SKU_TPU(topLogin)
        text_assert2 = page.SPU_SKU()

    @pytest.mark.p0
    def test_TPU(self, topLogin):
        # TPU菜单
        page = SKU_TPU(topLogin)
        text_assert3 = page.TPU()