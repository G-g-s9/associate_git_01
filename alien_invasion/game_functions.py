'''
辅助,主游戏的绝大多数函数都在这里
包含按键的多种响应、屏幕刷新等
*每个函数都尽量做到功能单一，不单一的，重构函数,最终要封装成独立功能
* 函数涉及直接调用的属性、类/模块都要写入形参
'''
import sys          # 导入sys模块（这里退出程序用）
from time import sleep
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
        
    elif event.key ==pygame.K_q:    #判断为按了Q 这个自己加的，按键习惯点😀
        sys.exit()      # 触发 SystemExit 异常来退出程序

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

def check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():        # 有事件发生就进入for循环
        if event.type == pygame.QUIT:       # 点击窗口关闭按钮,将检测到 pygame.QUIT 事件
            sys.exit()      # 触发 SystemExit 异常来退出程序

        elif event.type == pygame.KEYDOWN:  # 触发按键事件（按下）
            check_keydown_events(event,ai_settings,screen,ship,bullets)    # 跳转到按下响应函数

        elif event.type == pygame.KEYUP:    # 触发按键弹起
            check_keyup_events(event,ship)  # 跳转到按键弹起响应函数

        elif event.type == pygame.MOUSEBUTTONDOWN: #触发鼠标点击
            mouse_x,mouse_y = pygame.mouse.get_pos()    #获取点击位置元组坐标xy
            check_play_button(stats,play_button,mouse_x,mouse_y,
                            ai_settings,screen,aliens,ship,bullets,sb)    #跳转到👇

def check_play_button(stats,play_button,mouse_x,mouse_y,
                        ai_settings,screen,aliens,ship,bullets,sb):
    '''响应鼠标点击到按钮区域'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)  #bool 判断该坐标是否在对象play_button的rect区域内
    if button_clicked and not stats.game_active:        #同时满足点击区域在按键上，并且游戏是非活动状态
        #重置动态游戏参数
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)

        stats.reset_stats() #重置统计信息
        
        #刷新显示数值
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        stats.game_active = True    #活动状态转True

        #清空外星人和子弹
        aliens.empty()  #这两个都是清空group
        bullets.empty()

        #屏幕内对象都重置
        create_fleet(ai_settings,screen,aliens,ship)    #重新创建外星人群
        ship.center_ship()  #飞船居中

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
    number_rows = int(available_space_y / (2 * alien_height))+2    #间距为一行，设外星人间距为1个外星人高
    return number_rows      #返回行容纳量

def ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb):
    '''响应飞船被外星人撞到'''

    if stats.ships_left >0:
        #少一条命
        stats.ships_left -= 1
        sb.prep_ships() #更新神与命数

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕底部中央
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()

        #暂停
        sleep(0.5)  #推迟 0.5s调用线程，相当于进程挂起的时间 0.5s

    else:
        stats.game_active = False   #活动标志变为非
        pygame.mouse.set_visible(True)  #显示光标

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
    number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)   #容纳多少行

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

def check_high_score(stats,sb):
    '''检查新得分是否高于历史最高得分，是就在屏幕上更新最高得分image'''
    if stats.score > stats.high_score:  #新得分若大于历史最高分
        stats.high_score = stats.score  #新得分赋给最高值
        with open('high_score_value.txt','w') as fo:    #写入文档，记录历史最高得分（附加模式将更安全但会积累，后期可适当截取
            fo.write(str(stats.high_score))
        
        sb.prep_high_score()    #实时更新下历史最高得分
    
def change_fleet_direction(ai_settings,aliens):
    '''aliens下移，并转向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed    #向下闪现
    ai_settings.fleet_direction *= -1   #转向

def update_screen(ai_settings,screen,ship,bullets,aliens,stats,
                    play_button,sb):
    '''更新屏幕图像,并更新到整个屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)    # 填充色,最底层的最先填充,以防图层顺序的异常导致显示错误

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():        # 方法 bullets.sprites() 返回一个列表，包含子弹集中所有元素
        bullet.draw_bullet()     # 一一显示

    ship.blitme()   # 在指定位置绘制飞船
    aliens.draw(screen)  # 在指定位置绘制外星人
    
    #显示得分
    sb.show_score()

    #如果游戏处于 非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()   #更新整个显示，相当于刷新整个屏幕显示

def update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb):
    '''删除不在屏幕内的子弹'''
    bullets.update()    #刷新子弹
    for bullet in bullets.copy():   # 复制组
        if bullet.rect.bottom <= 0:     # 判断子弹的底部已不在屏幕内
            bullets.remove(bullet)      # 将该子弹从子弹集删除
    print('屏幕上有',len(bullets),'子弹')         # （这个加了验证子弹数的）后台实时显示子弹集元素个数

    check_bullet_alien_colisions(ai_settings,screen,aliens,ship,bullets,stats,sb)    # 调用下面👇的函数

def check_bullet_alien_colisions(ai_settings,screen,aliens,ship,bullets,stats,sb):
    '''检查是否有子弹击中外星人，碰撞就都删除；同时'''
    #如将第一个布尔实参dokill设置为 False ，第二个布尔实参为 True 。这样配置，碰撞后子弹无事，外星人消失
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)       #碰撞后双方都消失。pygame.sprite.groupcollide(group1,group2,dokill1,dokill2)
    
    if collisions:  #有一次碰撞  
        for aliens in collisions.values():  #遍历值   发生碰撞后返回字典 键-值对是{碰撞子弹:对应aliens}
            stats.score += ai_settings.alien_points * len(aliens) #记分+当前外星人分数*碰撞数量
            sb.prep_score() #更新分数图像（记分牌
        check_high_score(stats,sb)  #检查得分是否为新的最高得分

    if len(aliens) == 0:    #检测外星人是否光了
        #若清光外星人，则删除现有的子弹并新建一群外星人
        bullets.empty() #清空子弹集
        ai_settings.increase_speed()    #清空一遍后，速度就提升一次
        
        #玩家等级加一
        stats.level += 1
        sb.prep_level() #实时更新下等级
        
        create_fleet(ai_settings,screen,aliens,ship)    #重新创建外星人群

def check_aliens_bottom(stats,aliens,bullets,ai_settings,screen,ship,sb):
    '''检查有无外星人触底，冲破防线'''
    screen_rect = screen.get_rect()     #重新获取屏幕参数，以防手动调整过游戏窗口，从而造成错误
    for alien in aliens.sprites():      #遍历外星人集
        if alien.rect.bottom >= screen_rect.bottom:     #若有外星人的底边坐标大于等于屏幕底坐标，即触底
            #效果等同飞船被撞，都是玩家消耗一条命
            ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb)
            break       #有一个撞上就不用检查下去了

def update_aliens(stats,aliens,bullets,ai_settings,screen,ship,sb):
    '''检查外星人是否碰侧壁，是就更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)   #触碰响应
    aliens.update(ai_settings) #组合调用alien组的alien.update，更新位置

    #检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):     #检测，撞上返回ship，反之None
        ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb)  #调用飞船碰撞响应
        print("宝贝飞船被撞了")    #后台终端显示

    #检查有无外星人触底，冲破防线
    check_aliens_bottom(stats,aliens,bullets,ai_settings,screen,ship,sb)

