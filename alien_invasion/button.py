import pygame.font      #加载和表示文本模块

class Button():
    '''按键控件'''
    def __init__(self,screen,msg):      #？？ai_settings   self,ai_settings,screen,msg
        '''控件初始化属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #具体尺寸等
        self.width,self.height = 459,90     #这里创建的框小了，实际文字自带底色就会超出边界
        self.button_color = (135,135,135)   #灰色
        self.text_color = (255,255,255)     #白色
        self.font = pygame.font.Font('font/pingfang.ttf',48)    #pygame None默认字体，48号;试了几个常用字体，就苹方能正常显示中文

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height) #参数为左上角坐标xy，及宽高
        self.rect.center = self.screen_rect.center  #屏幕内居中

        #按钮标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''将字符串 msg渲染为图像，并使其在按钮上居中'''
        #pygame.font.font.render(字符串，抗锯齿True/False,字体颜色RGB元组，<可选>背景色)
        self.msg_image = self.font.render(msg,True,self.text_color,
                                        self.button_color)      #转化为surface
        self.msg_image_rect = self.msg_image.get_rect()     #获取文字层对应的surface的rect属性
        self.msg_image_rect.center = self.rect.center       #居中对齐建立的buttonrect对象

    def draw_button(self):
        '''绘制按钮'''
        self.screen.fill(self.button_color,self.rect)       #填充设置的按钮rect
        self.screen.blit(self.msg_image,self.msg_image_rect)    #在 文字层对应的surface的rect上绘制msg

