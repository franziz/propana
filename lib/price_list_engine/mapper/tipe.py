from .mapper import Mapper

class TipeMapper(Mapper):
	def __init__(self):
		Mapper.__init__(self)

	def map(self, based_on=None):
		Mapper.map(self, based_on)

		tipe = self.default
		if    based_on.lower() == "axis data & bb".lower() \
		   or based_on.lower() == "bolt".lower() \
		   or based_on.lower() == "indosat data dan BB".lower() \
		   or based_on.lower() == "indosat data promo".lower() \
		   or based_on.lower() == "indosat data promo ratu".lower() \
		   or based_on.lower() == "telkomsel data".lower() \
		   or based_on.lower() == "xl data dan bb".lower() \
		   or based_on.lower() == "smartfren paket data".lower() \
		   or based_on.lower() == "data three kartu aktif".lower() \
		   or based_on.lower() == "three (kpk)".lower() \
		   or based_on.lower() == "voucher fisik three".lower():
		   tipe = "KUOTA"

		if    based_on.lower() == "three".lower() \
		   or based_on.lower() == "inject saldo v-tri".lower() \
		   or based_on.lower() == "smartfren".lower() \
		   or based_on.lower() == "xl axis promo".lower() \
		   or based_on.lower() == "axis".lower() \
		   or based_on.lower() == "xl".lower() \
		   or based_on.lower() == "xl transfer".lower() \
		   or based_on.lower() == "indosat".lower() \
		   or based_on.lower() == "indosat promo".lower() \
		   or based_on.lower() == "indosat transfer".lower() \
		   or based_on.lower() == "telkomsel".lower() \
		   or based_on.lower() == "telkomsel promo".lower() \
		   or based_on.lower() == "telkomsel transfer".lower() \
		   or based_on.lower() == "voucher fisik three".lower():
		   tipe = "PULSA"

		if    based_on.lower() == "token pln murni".lower():
		   tipe = "TOKEN"

		if    based_on.lower() == "kuota telp three".lower() \
		   or based_on.lower() == "indosat sms & telp".lower() \
		   or based_on.lower() == "paket sms telkomsel".lower():
		   tipe = "PAKET"
		return tipe