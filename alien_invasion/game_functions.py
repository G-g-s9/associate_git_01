'''
辅助,主游戏的绝大多数函数都在这里
包含按键的多种响应、屏幕刷新等
*每个函数都尽量做到功能单一，不单一的，重构函数,最终要封装成独立功能
* 函数涉及直接调用的属性、类/模块都要写入形参
'''
import sys          # 导入sys模块（这里退出程序用）
import pygame       # 导入pygame模块，这种导入整个模块的都要用句点.表示法引用

from bullet import Bullet       # 导入子弹模块
from alien import Alien       # 导入alien.py模块中的Alien类


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''响应按下的函数'''
    if event.key == pygame.K_RIGHT:    # 判断为方向右移键
        ship.moving_right = True    # 右移标记为真
    elif event.key == pygame.K_LEFT:    # 判断为方向左移键   这里可以用 elif是因为每个按下时间都会判断一次,同时按键两个键都会被识别出来
        ship.moving_left = True    # 左移标记为真
    # 下面这段相当于是上下移动开关
    # ~ elif event.key == pygame.K_UP:    # 判断为up键
        # ~ ship.moving_top = True    # 上移标记为真
    # ~ elif event.key == pygame.K_DOWN:    # 判断为方down键
        # ~ ship.moving_bottom = True    # 下移标记为真

    # 追加子弹的空格响应
    elif event.key == pygame.K_SPACE:   # 判断为方向空格键
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):   # 弹起不需添加子弹相关属性
    '''响应弹起的函数'''
    if event.key == pygame.K_RIGHT:    # 判断为方向右移键
        ship.moving_right = False    # 右移标记为假
    elif event.key == pygame.K_LEFT:    # 判断为方向左移键
        ship.moving_left = False    # 左移标记为假
    elif event.key == pygame.K_UP:    # 判断为方向up键
        ship.moving_top = False    # 上移标记为假
    elif event.key == pygame.K_DOWN:    # 判断为方向下移键
        ship.moving_bottom = False    # 下移标记为假

def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():        # 有事件发生就进入for循环
        if event.type == pygame.QUIT:       # 点击窗口关闭按钮,将检测到 pygame.QUIT 事件
            sys.exit()      # 触发 SystemExit 异常来退出程序

        elif event.type == pygame.KEYDOWN:  # 触发按键事件（按下）
            check_keydown_events(event,ai_settings,screen,ship,bullets)    # 跳转到按下响应函数

        elif event.type == pygame.KEYUP:    # 触发按键弹起
            check_keyup_events(event,ship)  # 跳转到按键弹起响应函数

def fire_bullet(ai_settings,screen,ship,bullets):
    '''没到max，就发射子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship) #新建一个子弹实例
            bullets.add(new_bullet) #加入子弹集

def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行能容纳多少'''
    available_space_x = ai_settings.screen_width - 2*  alien_width  #假设可用空间两边各留一个外星人宽（计算用值，非实际情况
    number_aliens_x = int(available_space_x / (1.9 * alien_width))    #设外星人间距为0.9个外星人宽，算一行能容纳的外星人数（注意外星人数量比间距多1,而这里int截取整数后，看着最右边会有点空）
    return number_aliens_x      #返回一行容纳量

def get_number_rows(ai_settings,alien_height,ship_height):
    '''计算能容纳多少行'''
    available_space_y = ai_settings.screen_height - \
                        5 * alien_height - ship_height  #最上面最下面各空一行外星人高，再减去飞船高度
    number_rows = int(available_space_y / (2 * alien_height))    #间距为一行，设外星人间距为1个外星人高
    return number_rows      #返回行容纳量

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人，并放在当前行'''
    alien = Alien(ai_settings,screen)   #第一只（创建了，没加入GOUP，没显示
    alien_width = alien.rect.width  #获得一只外星人占用的宽数值
    alien.x = alien_width + 1.9 * alien_width * alien_number    #外星人水平坐标（浮点型），初始边距+（外星人宽+间距）*变量
    alien.rect.x = alien.x      #浮点型数值传给rext（只有整数部分，若优化游戏微控操作，精度后面有待提高）
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number   #初始y，加（外星人高+间距）
    aliens.add(alien)       #建好的外星人加入GOUP

def create_fleet(ai_settings,screen,aliens,ship):
    '''创建外星人群'''
    # 创建一个外星人，并计算每行可容纳多少个外星人
    alien = Alien(ai_settings,screen)   #创建一个
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)  #一行容纳量传递(参数宽是创建的那只的值，传给这个函数)
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x): #遍历创建一行
            #创建一个外星人并将其加入当前行
            creat_alien(ai_settings,screen,aliens,alien_number
                        ,row_number)

def check_fleet_edges(ai_settings,aliens):
        '''外星人触及边缘响应'''
        for alien in aliens.sprites():      #这里的精灵代码貌似可省略.sprites(),整理时试试
            if alien.check_edges(): #碰壁判断函数
                change_fleet_direction(ai_settings,aliens)  #aliens下移转向函数
                break   #终止循环

def change_fleet_direction(ai_settings,aliens):
    '''aliens下移，并转向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed    #向下闪现
    ai_settings.fleet_direction *= -1   #转向

def update_screen(ai_settings,screen,ship,bullets,aliens):
    '''更新屏幕图像,并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)    # 填充色,最底层的最先填充,以防图层顺序的异常导致显示错误

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():        # 方法 bullets.sprites() 返回一个列表，包含子弹集中所有元素
        bullet.draw_bullet()     # 一一显示

    ship.blitme()   # 在指定位置绘制飞船
    aliens.draw(screen)  # 在指定位置绘制外星人

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets,aliens,ai_settings,screen,ship):
    '''删除不在屏幕内的子弹'''
    bullets.update()    #刷新子弹
    for bullet in bullets.copy():   # 复制组
        if bullet.rect.bottom <= 0:     # 判断子弹的底部已不在屏幕内
            bullets.remove(bullet)      # 将该子弹从子弹集删除
    print(len(bullets))         # 后台实时显示子弹集元素个数
    #检查是否有子弹击中外星人，碰撞就都删除
    #如将第一个布尔实参dokill设置为 False ，第二个布尔实参为 True 。这样配置，碰撞后子弹无事，外星人消失
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)       #碰撞都消失。pygame.sprite.groupcollide(group1,group2,dokill1,dokill2)

    if len(aliens) == 0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)

def update_aliens(ai_settings,aliens):
    '''检查外星人是否碰壁，是就更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)   #触碰响应
    aliens.update(ai_settings) #组合调用alien组的alien.update，更新位置

