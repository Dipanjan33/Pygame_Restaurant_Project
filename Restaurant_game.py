import pygame
from sys import exit

food_list = [
    {'name':'Rice','price':6},
    {'name':'Fish','price':15},
    {'name':'Bread','price':6},
    {'name':'Salad','price':5},
    {'name':'Water','price':2},
    {'name':'Chicken','price':18}
]

total = 0
game_active = 1

def print_item(rect_list):
    global total
    if rect_list:
        for i,rect in enumerate(rect_list):
            # if i > 5: 
            #     food_rect_list.clear()
            #     total = 0
            if rect == rice_rect:
                text = f"{food_list[0]['name']}  ${food_list[0]['price']}"
            if rect == fish_rect:
                text = f"{food_list[1]['name']}  ${food_list[1]['price']}"
            if rect == bread_rect:
                text = f"{food_list[2]['name']}  ${food_list[2]['price']}"
            if rect == salad_rect:
                text = f"{food_list[3]['name']}  ${food_list[3]['price']}"
            if rect == water_rect:
                text = f"{food_list[4]['name']}  ${food_list[4]['price']}"
            if rect == chicken_rect:
                text = f"{food_list[5]['name']}  ${food_list[5]['price']}"
            text_surf = food_item_font.render(text,True,'White')
            text_rect = text_surf.get_rect(center = (800,(55+i*30)))
            screen.blit(text_surf,text_rect)
                


pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Restaurant Game')
clock = pygame.time.Clock()
food_item_font = pygame.font.SysFont('arial',20)


restaurant_backdrop = pygame.image.load('graphics/restaurant_image.jpg').convert()

menu_surf = pygame.Surface((350,450))
menu_surf.fill((26,31,27.4))

text1_surf = food_item_font.render('Item  Subtotal',True,'White')
text1_rect = text1_surf.get_rect(center = (800,35))



rice_surf = pygame.Surface((175,200))
rice_surf.fill((17.3,1.3,6))
rice_rect = rice_surf.get_rect(topleft = (25,25))

fish_surf = pygame.Surface((175,200))
fish_surf.fill((17.3,1.3,6))
fish_rect = fish_surf.get_rect(topleft = (225,25))

bread_surf = pygame.Surface((175,200))
bread_surf.fill((17.3,1.3,6))
bread_rect = bread_surf.get_rect(topleft = (425,25))

salad_surf = pygame.Surface((175,200))
salad_surf.fill((17.3,1.3,6))
salad_rect = salad_surf.get_rect(topleft = (25,250))

water_surf = pygame.Surface((175,200))
water_surf.fill((17.3,1.3,6))
water_rect = water_surf.get_rect(topleft = (225,250))

chicken_surf = pygame.Surface((175,200))
chicken_surf.fill((17.3,1.3,6))
chicken_rect = chicken_surf.get_rect(topleft = (425,250))

rice_pic = pygame.image.load('graphics/Foods/rice.png').convert_alpha()
rice_pic_rect = rice_pic.get_rect(midtop = (112.5,25))

fish_pic = pygame.image.load('graphics/Foods/fish.png').convert_alpha()
fish_pic_rect = fish_pic.get_rect(midtop = (312.5,25))

bread_pic = pygame.image.load('graphics/Foods/bread.png').convert_alpha()
bread_pic_rect = bread_pic.get_rect(midtop = (512.5,25))

salad_pic = pygame.image.load('graphics/Foods/salad.png').convert_alpha()
salad_pic_rect = salad_pic.get_rect(midtop = (112.5,250))

water_pic = pygame.image.load('graphics/Foods/water.png').convert_alpha()
water_pic_rect = water_pic.get_rect(midtop = (312.5,250))

chicken_pic = pygame.image.load('graphics/Foods/chicken.png').convert_alpha()
chicken_pic_rect = chicken_pic.get_rect(midtop = (512.5,250))

food_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rice_rect.collidepoint(event.pos):
                food_rect_list.append(rice_rect)
                total += food_list[0]['price']
            if fish_rect.collidepoint(event.pos):
                food_rect_list.append(fish_rect)
                total += food_list[1]['price']
            if bread_rect.collidepoint(event.pos):
                food_rect_list.append(bread_rect)
                total += food_list[2]['price']
            if salad_rect.collidepoint(event.pos):
                food_rect_list.append(salad_rect)
                total += food_list[3]['price']
            if water_rect.collidepoint(event.pos):
                food_rect_list.append(water_rect)
                total += food_list[4]['price']
            if chicken_rect.collidepoint(event.pos):
                food_rect_list.append(chicken_rect)
                total += food_list[5]['price']
        

                
                

    if game_active:
        screen.blit(restaurant_backdrop,(-75,-200))
        screen.blit(menu_surf,(625,25))
        screen.blit(text1_surf,text1_rect)

        total_text_surf = food_item_font.render(f'Total = {total}',True,'White')
        total_text_rect = total_text_surf.get_rect(center = (800,400))
        screen.blit(total_text_surf,total_text_rect)

        confirm_text_surf = food_item_font.render('Confirm Order',True,'White')
        confirm_text_rect = confirm_text_surf.get_rect(center = (800,430))
        pygame.draw.rect(screen,'red',confirm_text_rect)
        pygame.draw.rect(screen,'red',confirm_text_rect,10)
        screen.blit(confirm_text_surf,confirm_text_rect)
        
        screen.blit(rice_surf,rice_rect)
        screen.blit(fish_surf,fish_rect)
        screen.blit(bread_surf,bread_rect)
        screen.blit(salad_surf,salad_rect)
        screen.blit(water_surf,water_rect)
        screen.blit(chicken_surf,chicken_rect)

        screen.blit(rice_pic,rice_pic_rect)
        screen.blit(fish_pic,fish_pic_rect)
        screen.blit(bread_pic,bread_pic_rect)
        screen.blit(salad_pic,salad_pic_rect)
        screen.blit(water_pic,water_pic_rect)
        screen.blit(chicken_pic,chicken_pic_rect)
        

        print_item(food_rect_list)

        mouse_press = pygame.mouse.get_pressed()

        if mouse_press[0] and confirm_text_rect.collidepoint(event.pos):
            game_active = 0
    
    else:
        screen.fill((18.2,91.1,17))
        food_rect_list.clear()
        total = 0

        Thank_You_Font =pygame.font.SysFont('timesnewroman',50)
        ty_text_surf = Thank_You_Font.render("Thank you for your order",True,'Black')
        ty_text_rect = ty_text_surf.get_rect(center = (500,130))
        screen.blit(ty_text_surf,ty_text_rect)

        reorder_text_surf = Thank_You_Font.render('Order Again',True,'White')
        reorder_text_rect = reorder_text_surf.get_rect(center = (500,260))
        pygame.draw.rect(screen,'red',reorder_text_rect)
        pygame.draw.rect(screen,'red',reorder_text_rect,50)
        screen.blit(reorder_text_surf,reorder_text_rect)

        mouse_press = pygame.mouse.get_pressed()

        if mouse_press[0] and reorder_text_rect.collidepoint(event.pos):
            game_active = 1



    pygame.display.update()
    clock.tick(60)