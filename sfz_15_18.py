



class sfz_15_18(object):
	def __init__(self,sfz):
		self.sfz_18=""
		self.sfz_15=""
		if len(sfz)==18:
			self.sfz_18=sfz
		elif len(sfz)==15:
			self.sfz_15=sfz
	def  jiaquan(self,n):
		w=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
		s=0
		for i in range(17):
			s+=n[i]*w[i]
		return s
	def last_num(self,n):
		s=self.jiaquan(n)
		y=s%11
		zidian={0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
		return zidian[y]
	def yanzheng(self):
		n=[]
		for i in self.sfz_18[:-1]:
			n.append(int(i))
		last=self.last_num(n)
		if last==self.sfz_18[-1]:
			print last,self.sfz_18[-1]
			return True
		else:
			return False
	def buquan(self):
		n=[]
		for i in self.sfz_15[:6]:
			n.append(int(i))
		n.append(1)
		n.append(9)
		for i in self.sfz_15[6:]:
			n.append(int(i))
		last=self.last_num(n)
		n.append(int(last))
		s=""
		for i in n:
			s+=str(i)
		return s
	def is_sfz(self):
		return bool(self.sfz_15 or self.sfz_18)
if __name__=="__main__":
	s=raw_input("sfz:")
	x=sfz_15_18(s)
	print x.is_sfz()
	




