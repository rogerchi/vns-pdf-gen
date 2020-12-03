#encoding:utf8
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.lib.units import cm
from reportlab.lib.units import mm
import math
#This program draws the shape of a vertical sector of a VNS EQ platform
#Details please refere http://www.reinervogel.net/index_e.html?/Plattform/plattform_VNS_e.html
#Please change next EQ platform varaiables to fit your design;

def generate_pdf(primarylength=850, latitude_degree=40, half_string_len=350, size_str="A4"):

  # primarylength=850
  # latitude_degree=40
  # half_string_len=350
  try:
    size = getattr(pagesizes, size_str)
  except:
    raise Exception(f'Size {size_str} not found')

  beta=45/2/180*math.pi
  latitude=latitude_degree/180*math.pi

  def draw_axis(c):
    # x axis:
    c.line(0,0,15*cm,0)
    for i in range(1,16):
      c.line(i*cm,0,i*cm,0.2*cm)
      c.drawString((i-0.2)*cm,-0.5*cm, str(i))
    c.drawString(15.3*cm,-0.5*cm, "cm")
    # y axis:
    c.line(0,0,0,28*cm)
    for i in range(1,28):
      c.line(0,i*cm,0.2*cm,i*cm)
      c.drawString(-1*cm, i*cm, str(i))
    c.drawString(-0.6*cm, 27*cm, "cm")
  def draw_schema(c):
    #顶板结构示意 To draw the shape of top board
    c.setStrokeColorRGB(0,0,1)
    c.setFillColorRGB(0,0,1)
    c.line(4*cm,12*cm, (4-primarylength/100*math.sin(beta))*cm,(12-primarylength/100*math.cos(beta))*cm)
    c.line((4-primarylength/100*math.sin(beta))*cm,(12-primarylength/100*math.cos(beta))*cm,4*cm,(12-primarylength/100/math.cos(beta))*cm)
    c.line(4*cm,(12-primarylength/100/math.cos(beta))*cm,(4+primarylength/100*math.sin(beta))*cm,(12-primarylength/100*math.cos(beta))*cm)
    c.line((4+primarylength/100*math.sin(beta))*cm,(12-primarylength/100*math.cos(beta))*cm,4*cm,12*cm)

    c.drawString((4-primarylength/100*math.sin(beta)+0.3)*cm,(12-primarylength/100*math.cos(beta)-0.2)*cm, "90°")
    c.drawString((4+primarylength/100*math.sin(beta)-0.8)*cm,(12-primarylength/100*math.cos(beta)-0.2)*cm, "90°")
    c.drawString((4-0.2)*cm,(12-1.5)*cm, "45°")

    c.drawString((4+primarylength/100*math.sin(beta)-0.1)*cm,(12-primarylength/100*math.cos(beta)+0.8)*cm,"2.5cm")
    c.line((4+primarylength/100*math.sin(beta)+0.1)*cm,(12-primarylength/100*math.cos(beta)+0.05)*cm,(4+primarylength/100*math.sin(beta)+0.1)*cm,(12-primarylength/100*math.cos(beta)+0.7)*cm)
  #	c.line((4+primarylength/100*math.sin(beta)+0.1)*cm,(12-primarylength/100*math.cos(beta))*cm,(4+primarylength/100*math.sin(beta)-0.1)*cm,(12-primarylength/100*math.cos(beta)+0.1)*cm)
  #	c.line((4+primarylength/100*math.sin(beta)+0.1)*cm,(12-primarylength/100*math.cos(beta))*cm,(4+primarylength/100*math.sin(beta)+0.2)*cm,(12-primarylength/100*math.cos(beta)+0.1)*cm)

    #标注顶板主尺寸：size dimensioning
    c.line((4-0.6)*cm,(12+0.2)*cm, (4-primarylength/100*math.sin(beta)-0.6)*cm,(12-primarylength/100*math.cos(beta)+0.3)*cm)
    c.line((4-0.6-0.1)*cm,(12+0.2+0.03)*cm,(4-0.6+0.1)*cm,(12+0.2-0.03)*cm,)
    c.line((4-primarylength/100*math.sin(beta)-0.6-0.1)*cm,(12-primarylength/100*math.cos(beta)+0.3+0.03)*cm,(4-primarylength/100*math.sin(beta)-0.6+0.1)*cm,(12-primarylength/100*math.cos(beta)+0.3-0.03)*cm)
    c.drawString(1*cm,(12-primarylength/100*math.cos(beta)/2)*cm, str(primarylength))
    c.drawString(3*cm,7*cm, "Altitude="+str(latitude_degree)+ " °")
    #标注滑扇整弦长。这个长度比顶板北端宽度稍微宽一点，滑扇尖超出2.5CM. The vertical sector extrude out 2.5cm from the top board to fit the thinkness of top board.
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.line((4-primarylength/100*math.sin(beta)-0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2)*cm,(4+primarylength/100*math.sin(beta)+0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2)*cm)
    c.line((4-primarylength/100*math.sin(beta)-0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2-0.1)*cm,(4-primarylength/100*math.sin(beta)-0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2+0.1)*cm)
    c.line((4+primarylength/100*math.sin(beta)+0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2-0.1)*cm,(4+primarylength/100*math.sin(beta)+0.2)*cm,(12-primarylength/100*math.cos(beta)+0.2+0.1)*cm)
    c.drawString((4-0.3)*cm,(12-primarylength/100*math.cos(beta)+0.2+0.1)*cm, str(int(half_string_len*2)))
    #用黑线画出滑扇投影 To draw vertical projection of the sector in black.
    c.setLineWidth(2)
    c.line((4-primarylength/100*math.sin(beta)-0.2)*cm,(12-primarylength/100*math.cos(beta))*cm,(4-primarylength/100*math.sin(beta)/2-0.2)*cm,(12-primarylength/100/math.cos(beta)+half_string_len/100*math.tan(beta)/2-0.05)*cm)
    c.line((4+primarylength/100*math.sin(beta)/2+0.2)*cm,(12-primarylength/100/math.cos(beta)+half_string_len/100*math.tan(beta)/2-0.05)*cm,(4+primarylength/100*math.sin(beta)+0.2)*cm,(12-primarylength/100*math.cos(beta))*cm)
    c.setLineWidth(1)


  def draw_sector(c):
    # the sector:
    sectorpoints=[]
    sectorpoints_alpha=[]
    sectorpoints_alpha_beta=[]
    r=primarylength*math.sin(latitude)
    l=r*math.cos(math.asin(half_string_len/r))
    #计算扇区数据，分圆周、高*cos(a)、长/cos(b)且高*cos(a)，三份数据. To draw three line: the cycle, *cos(a) and *cos(a)/cos(b), use the black one to cut your sector.
    for i in range(0,int(275*mm)):
      y=half_string_len-i/mm
      x=(r**2-y**2)**0.5
  #		if i%(int(cm)) == 0 :
  #			print((x,y))
      sectorpoints.append(((x-l)*mm,(y-80)*mm))
      sectorpoints_alpha.append(((x-l)*math.cos(latitude)*mm,(y-80)*mm))
      sectorpoints_alpha_beta.append(((x-l)*math.cos(latitude)*mm,(half_string_len-i/mm/math.cos(beta)-80)*mm))
    #画滑扇：to draw the sector
    for i in range(1,int(275*mm)):
      #Cycle
      c.setStrokeColorRGB(1,0,0)
      c.setFillColorRGB(1,0,0)
      c.line(sectorpoints[i-1][0],sectorpoints[i-1][1], sectorpoints[i][0],sectorpoints[i][1])
      if i%(int(5*cm)) == 0 :
        c.line(sectorpoints[i][0],sectorpoints[i][1],sectorpoints[i][0]+3,sectorpoints[i][1])
      if i == int(20*cm):
        c.drawString(sectorpoints[i][0],sectorpoints[i][1]-0.3*cm, "Circle")
      # x*cos(a)
      c.setStrokeColorRGB(0,1,0)
      c.setFillColorRGB(0,1,0)
      c.line(sectorpoints_alpha[i-1][0],sectorpoints_alpha[i-1][1], sectorpoints_alpha[i][0],sectorpoints_alpha[i][1])
      if i%(int(5*cm)) == 0 :
        c.line(sectorpoints_alpha[i][0],sectorpoints_alpha[i][1],sectorpoints_alpha[i][0]+3,sectorpoints_alpha[i][1])
      if i == int(22*cm):
        c.drawString(sectorpoints_alpha[i][0],sectorpoints_alpha[i][1]-0.3*cm, "Circle*cos(a)")
      # x*cos(a),y/cos(b)
      c.setStrokeColorRGB(0,0,0)
      c.setFillColorRGB(0,0,0)
      c.line(sectorpoints_alpha_beta[i-1][0],sectorpoints_alpha_beta[i-1][1], sectorpoints_alpha_beta[i][0],sectorpoints_alpha_beta[i][1])
      if i%(int(5*cm)) == 0 :
        c.line(sectorpoints_alpha_beta[i][0],sectorpoints_alpha_beta[i][1],sectorpoints_alpha_beta[i][0]+3,sectorpoints_alpha_beta[i][1])
      if i == int(23*cm):
        c.drawString(sectorpoints_alpha_beta[i][0],sectorpoints_alpha_beta[i][1]-0.3*cm, "Circle*cos(a)/cos(b)")
  filename = f"/tmp/vnc-pl_{str(primarylength)}-hsl_{str(half_string_len)}-lat_{str(latitude_degree)}-size_{size_str}.pdf"
  c = canvas.Canvas(filename,pagesize=size)
  # move the origin up and to the right
  c.translate(5*cm,1*cm)
  draw_axis(c)
  draw_schema(c)
  draw_sector(c)
  c.showPage()
  c.save()
  print("Finished, please check:"+filename)
  return filename


