'''
显示event.key，则是ASCII码值
显示event，则是（下面a键event）
<Event(2-key Down {'unicode':'a', 'key': 97, 'mod': 4096, 'scancode': 38, 'window': None})>
'''import sys
import pygame

def run_textkey():
    '''每当检测到 pygame.KEYDOWN 事件时都打印属性 event.key，结果显示的是ascii码值'''
    pygame.init()       #初始化
    screen = pygame.display.set_mode([900,400]) #建立窗口
    pygame.display.set_caption('显示按键 pyame.event.key 名')    #标题

    gt = pygame.font.Font(None,28)   #建立字体对象，并初始化参数
    screen.fill((149,249,199))      #先变色，算是初始等待页，加载页


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            else:
                if event.type == pygame.KEYDOWN:    # 检测到按键反应

                    #以下两种皆可
                    # ~ text_content = str(event.key)   #显示的是ASCII码值
                    text_content = str(event)   #显示的。。嗯。很全，还不了解

                    #渲染成一个surface对象。第一个参数是显示的内容，第二个参数是否消除锯齿，第三个参数颜色，此处是宝蓝色
                    text_content = gt.render(text_content,True,(20,20,128))

                    # ~ #显示位置调整，这里无用（被blit定住了
                    # ~ text_rect = text_content.get_rect()
                    # ~ screen_rect = screen.get_rect()
                    # ~ text_rect.left =  screen_rect.left-200

                    screen.fill((190,255,235))
                    screen.blit(text_content,(19,200))  #blit两个参数，字符串、位置坐标




        pygame.display.flip()


run_textkey()


# ~ pygame.init()
# ~ screen=pygame.display.set_mode((600,500))
# ~ myfont=pygame.font.Font(None,60)
# ~ white=255,255,255
# ~ blue=0,0,255
# ~ textImage=myfont.render("Hello Pygame",True,white)
# ~ screen.fill(blue)

# ~ screen.blit(textImage,(100,100))

# ~ pygame.display.update()
