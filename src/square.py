import PySimpleGUI as sg

from abc import ABCMeta, abstractmethod
import os

from .Color import Color
from config import IMAGE_ROOT

class Square(metaclass=ABCMeta): 
    def __bool__(self) -> bool:
        return bool(int(self))

    def __eq__(self, other) -> bool:
        return int(self) == int(other)

    def __hash__(self) -> bool:
        return hash(int(self))

    @abstractmethod
    def __int__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return str(int(self))

    def __xor__(self, other) -> int:
        return Pawn() if int(self) ^ int(other) else Blank()
    
    @abstractmethod
    def image_name(self) -> str:
        pass
    
    def get_image_path(self) -> str:
        return os.path.join(IMAGE_ROOT, self.image_name()) 

    def rendered_at(
            self,
            location: tuple[int, int],
            light_color: str=Color.khaki,
            dark_color:str=Color.peru,
        ) -> sg.PySimpleGUI.ReadButton: 
        """位置座標を元にしたセルの描画

        Args:
            location (tuple[int, int]): 配置する座標
            light_color (str): 明色
            dark_color (str): 暗色

        Returns:
            PySimpleGUI.PySimpleGUI.ReadButton: 画像を埋め込んだReadButton
        """
        color = dark_color if (location[0] + location[1]) % 2 else light_color
        
        return sg.ReadButton(
            '',
            image_filename=self.get_image_path(),
            size=(1, 1),
            border_width=0,
            button_color=('white', color),
            pad=(0, 0),
            disabled=True,
            key=location
        )
    

class Blank(Square):
    def __int__(self) -> int:
        return 0
    
    def __repr__(self) -> str:
        return "Blank"
    
    def image_name(self) -> str:
        return 'blank.png'


class Pawn(Square):
    def __int__(self) -> int:
        return 1
    
    def __repr__(self) -> str:
        return "Pawn"
    
    def image_name(self) -> str:
        return 'pawn.png'