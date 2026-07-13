import pygame

'''
A classe Object representa um objeto padrão do PyGame.
Para ela, precisamos saber a posição (x, y) do objeto e a cena na qual ele pertence.
O método update é chamado a cada frame caso o objeto precise ser renderizado.
'''
class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.scene = None

    def set_scene(self, scene):
        if scene != None and not isinstance(scene, Scene):
            raise TypeError("scene must be an instance of Scene class")
        self.scene = scene

    def update(self, surface, delta_time):
        raise NotImplementedError("Subclasses must implement this method.")

    def set_position(self, x, y):
        self.x = x
        self.y = y

'''
Uma variação da classe object, mas que renderiza uma imagem.
Não foi utilizado na versão final.
'''
class Sprite(Object):
    def __init__(self, x, y, image_path, scale=1.0):
        super().__init__(x, y)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.offset_x = self.image.get_width() // 2
        self.offset_y = self.image.get_height() // 2

    def update(self, surface, delta_time):
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.image, (self.x - self.offset_x, self.y - self.offset_y))

'''
A classe Text representa um texto.
Foi criada posteriormente para facilitar o desenvolvimento, mas não foi utilizada na versão final.
'''
class Text(Object):
    def __init__(self, x, y, text, font_size=24, color=(0, 0, 0)):
        super().__init__(x, y)
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)
        self.visible = True

    def update(self, surface, delta_time):
        self.draw(surface)

    def draw(self, surface):
        if self.visible:
            text_surface = self.font.render(self.text, True, self.color)
            surface.blit(text_surface, (self.x, self.y))

    def set_visible(self, visible):
        self.visible = visible

    def set_text(self, text):
        self.text = text

'''
A classe Scene representa uma cena, ou seja, tudo que está sendo renderizado ao mesmo tempo.
Sua função é atualizar todos os objetos que estão inseridos nela, chamando o método update de cada um.
Apenas cria uma forma simples de lidar com os Objects, sem fazer bagunça no main.
'''
class Scene:
    def __init__(self, surface):
        self.surface = surface
        self.objects = []

    def add_object(self, obj):
        if not isinstance(obj, Object):
            raise TypeError("obj must be an instance of Object class")
        self.objects.append(obj)
        obj.set_scene(self)

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
            obj.set_scene(None)

    def update(self, delta_time):
        for obj in self.objects:
            obj.update(self.surface, delta_time)
