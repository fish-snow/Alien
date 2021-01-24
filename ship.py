import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        # 初始化飞船并设置其初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('外星人入侵\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动标志调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
        # if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
        # if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)