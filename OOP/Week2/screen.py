#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# ==================================
class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2d(self.x * other, self.y * other)

    def __len__(self):
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def int_pair(self):
        return self.x, self.y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y

    # def __str__(self):
    #     return f'X = {self.x} Y = {self.y}'
    #
    # def __repr__(self):
    #     return f'X = {self.x} Y = {self.y}'


# ==================================
class Polyline:
    def __init__(self, points=None, speeds=None):
        if speeds is None:
            speeds = []
        if points is None:
            points = []
        self.points = points
        self.speeds = speeds

    def append(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def remove(self, item):
        for point in self.points:
            if item.x - 4 <= point.x <= item.x + 4 and item.y - 4 <= point.y <= item.y + 4:
                index = self.points.index(point)
                break

        del self.points[index]
        del self.speeds[index]

    def __contains__(self, item):
        for point in self.points:
            if item.x - 4 <= point.x <= item.x + 4 and item.y - 4 <= point.y <= item.y + 4:
                return True
        return False

    def set_points(self):
        """С„СѓРЅРєС†РёСЏ РїРµСЂРµСЂР°СЃС‡РµС‚Р° РєРѕРѕСЂРґРёРЅР°С‚ РѕРїРѕСЂРЅС‹С… С‚РѕС‡РµРє"""
        for i in range(len(self.points)):
            self.points[i] = self.points[i] + self.speeds[i]
            if self.points[i][0] > SCREEN_DIM[0] or self.points[i][0] < 0:
                self.speeds[i] = Vec2d(- self.speeds[i][0], self.speeds[i][1])
            if self.points[i][1] > SCREEN_DIM[1] or self.points[i][1] < 0:
                self.speeds[i] = Vec2d(self.speeds[i][0], -self.speeds[i][1])

    def draw_points(self, points=None, style="points", width=3, color=(255, 255, 255), display=None):
        """С„СѓРЅРєС†РёСЏ РѕС‚СЂРёСЃРѕРІРєРё С‚РѕС‡РµРє РЅР° СЌРєСЂР°РЅРµ"""
        if points == None:
            points = self.points

        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(display, color,
                                 (points[p_n][0], points[p_n][1]),
                                 (points[p_n + 1][0], points[p_n + 1][1]), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(display, color,
                                   (p[0], p[1]), width)


# ==================================
class Knot(Polyline):
    def __init__(self):
        super().__init__()
        self.steps = 50

    def reset(self):
        self.points = []
        self.speeds = []
        self.steps = 50

    @staticmethod
    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + Knot.get_point(points, alpha, deg - 1) * (1 - alpha)

    @staticmethod
    def get_points(base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Knot.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(Knot.get_points(ptn, self.steps))
        return res


def draw_help(lines_list, current):
    """С„СѓРЅРєС†РёСЏ РѕС‚СЂРёСЃРѕРІРєРё СЌРєСЂР°РЅР° СЃРїСЂР°РІРєРё РїСЂРѕРіСЂР°РјРјС‹"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["A", "Add line"])
    data.append(["D", "Delete current line"])
    data.append(["N", "Next line"])
    data.append([str(len(lines_list)), "Number of lines"])
    data.append([str(current + 1), "Current line"])
    data.append(["", ""])
    data.append([str(lines_list[current].steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# РћСЃРЅРѕРІРЅР°СЏ РїСЂРѕРіСЂР°РјРјР°
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True

    lines_list = [Knot()]
    current = 0

    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    lines_list[current].reset()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_a:
                    lines_list.append(Knot())
                    current += 1
                if event.key == pygame.K_d:
                    del lines_list[current]
                    current -= 1
                    if current == -1:
                        lines_list = [Knot()]
                        current = 0
                if event.key == pygame.K_n:
                    current = (current + 1) % (len(lines_list))
                if event.key == pygame.K_KP_PLUS:
                    lines_list[current].steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    lines_list[current].steps -= 1 if lines_list[current].steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                point = Vec2d(event.pos[0], event.pos[1])
                speed = Vec2d(random.random() * 2, random.random() * 2)
                if point in lines_list[current]:
                    lines_list[current].remove(point)
                else:
                    lines_list[current].append(point, speed)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        for line in lines_list:
            line.draw_points(display=gameDisplay)
            line.draw_points(points=line.get_knot(), style="line", width=3, color=color, display=gameDisplay)

        if not pause:
            for line in lines_list:
                line.set_points()
        if show_help:
            draw_help(lines_list, current)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)