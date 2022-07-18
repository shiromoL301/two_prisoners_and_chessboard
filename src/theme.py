from __future__ import annotations

from .Color import Color
from .Font import Font

class ColorTheme:
    def __init__(
        self,
        background_color: str,
        title_color: str,
        text_color: str,
        accent_color: str,
        square_light_color: str,
        square_dark_color: str,
    ):
        self.__accent_color = accent_color
        self.__background_color = background_color
        self.__square_light_color = square_light_color
        self.__square_dark_color = square_dark_color
        self.__text_color = text_color
        self.__title_color = title_color
    
    @property
    def accent_color(self) -> str:
        return self.__accent_color
    
    @property
    def background_color(self) -> str:
        return self.__background_color
     
    @property
    def square_light_color(self) -> str:
        return self.__square_light_color
    
    @property
    def square_dark_color(self) -> str:
        return self.__square_dark_color
    
    @property
    def text_color(self) -> str:
        return self.__text_color

    @property
    def title_color(self) -> str:
        return self.__title_color

    @classmethod
    def monochrome(self) -> ColorTheme:
        return ColorTheme(
            background_color   = Color.white,
            square_light_color = Color.lightgray,
            square_dark_color  = Color.gray,
            title_color        = Color.black,
            text_color         = Color.black,
            accent_color       = Color.darkslategray
        )
    
    @classmethod
    def reddit(self) -> ColorTheme:
        return ColorTheme(
            background_color   = Color.white,
            square_light_color = Color.khaki,
            square_dark_color  = Color.peru,
            title_color        = Color.midnightblue,
            text_color         = Color.black,
            accent_color       = Color.crimson
        )
    
    @classmethod
    def seagreen(self) -> ColorTheme:
        return ColorTheme(
            background_color   = Color.darkseagreen,
            square_light_color = Color.lightseagreen,
            square_dark_color  = Color.seagreen,
            title_color        = Color.darkslategray,
            text_color         = Color.black,
            accent_color       = Color.crimson
        )
    
    @classmethod
    def skyblue(self) -> ColorTheme:
        return ColorTheme(
            background_color   = Color.lightblue,
            square_light_color = Color.lightskyblue,
            square_dark_color  = Color.steelblue,
            title_color        = Color.midnightblue,
            text_color         = Color.black,
            accent_color       = Color.crimson
        )


class FontTheme:
    def __init__(
        self,
        title_font: str,
        text_font: str,
        accent_font: str
    ):
        self.__title_font  = title_font
        self.__text_font   = text_font
        self.__accent_font = accent_font
        
    @property
    def accent_font(self) -> str:
        return self.__accent_font
    
    @property
    def text_font(self) -> str:
        return self.__text_font
    
    @property
    def title_font(self) -> str:
        return self.__title_font
     
    @classmethod
    def natural(self) -> FontTheme:
        return FontTheme(
            title_font=Font.biz_udp_gothic,
            text_font=Font.biz_ud_gothic,
            accent_font=Font.hg_maru_gothic_m_pro
        )
    
    @classmethod
    def arial(self) -> FontTheme:
        return FontTheme(
            title_font=Font.arial,
            text_font=Font.arial,
            accent_font=Font.arial
        )


class GuiTheme:
    def __init__(
        self,
        color_theme: ColorTheme,
        font_theme: FontTheme = FontTheme.arial()
    ):
        self.__color_theme: ColorTheme = color_theme
        self.__font_theme: FontTheme = font_theme
    
    @property
    def color_theme(self) -> ColorTheme:
        return self.__color_theme
    
    @property
    def font_theme(self) -> FontTheme:
        return self.__font_theme
    
    @classmethod
    def reddit(self) -> GuiTheme:
        return GuiTheme(
            color_theme = ColorTheme.reddit(),
            font_theme  = FontTheme.arial()
        )