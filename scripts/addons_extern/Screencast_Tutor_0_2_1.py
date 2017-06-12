#-----------------------------------------------------------------------------------
# Terms and Conditions
#-----------------------------------------------------------------------------------
#
#Screencast Tutor 0.2.1 - A visual tutorial aid to display events in Blender's 3d view
#Copyright (C) 2011  Giles Bayliss
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
#-----------------------------------------------------------------------------------
# Known issues and features
#-----------------------------------------------------------------------------------
#
# The fade out on the overlayed icons is driven by redundant events (i.e mousemove)
# I haven't had time to find a way of triggering a redraw without locking up the
# the interface but I suspect that with a little digging and some help with the guys
# on IRC this may be possible.  They're busy getting the next stable release out so
# I've avoided such frivolities thus far.
#
# Some events cannot be captured (must wait for blender event system to be updated) 
#  i.e constraining axes during grab/rotate/translate/extrude so I have implemented a
# help bar during these modes.
#
# I realize that the first 50 lines is purely commentary so apologies but I would like
# to get it off my chest
#
# I never did get time to look at the splashscreen on starting the script. Sorry
#
# I only learned (barely) how to write python this last week or so.
# I know it's not perfect and a lot of it was done wiht very little sleep
# but I've tried to comment where I can and use classes and overrides where possible
# to maximise re-use.
#
#-----------------------------------------------------------------------------------
# Honors and mentions
#-----------------------------------------------------------------------------------
#
# This script was inspired by the Screencast_Keys script by Paulo Gomes.
# The aforementioned script was heroically maintained by Crouch. As such, I
# feel it only right to honor their efforts.
# 
# This script was written from the ground up and does not borrow any of the code from
# the aforementioned authors. It does however borrow the use of the 'F7' key to halt
# execution of the operator
#
# The only common code is from the script templates and that necessitated by the
# blender python api.
#
# If you have any questions regarding this please do not hesitate to contant me.
#
# Finally thanks go to:
#
#   MikeyB and RobinP for allowing me the time off work to indulge in this project
#   Ton, Bart and the rest of the blender guys who made all this possible 
#   Olson, for keeping me company on the irc graveyard shift and his testing this
#   Lumpycow for his awesome irc nick, always makes me smile ;)
#   Andrew Price for his great tuts
#   To everybody who has contributed code, scipts, docs, tuts and precious time in
#   the name of blender, I sympathize with your passion and pain.
#
#-----------------------------------------------------------------------------------
# Blender Addon information (required for 2.56+)
#-----------------------------------------------------------------------------------

bl_info = \
    {
        "name" : "Screencast Tutor",
        "author" : "jiggles100",
        "version" : (0,2,1),
        "blender" : (2, 5, 6),
        "api" : 32411,
        "location" : "View 3D > Screencast Tutor",
        "description" : "Tutorial Annotation System - tested with API 2.56.1 UNSTABLE",
        "warning" : "",
        "wiki_url" : "",
        "tracker_url" : "",
        "category" : "3D View",
    }


#-----------------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------------

import bpy
import bgl
import blf
import time


#-----------------------------------------------------------------------------------
# Overlay uAPI
#-----------------------------------------------------------------------------------
#
# This micro API (uAPI) provides an abstraction layer for displaying the controls
# overlayed on the 3D view. The drawing functions are performed using the bgl wrapper
# for opengl functions.  Please refer to the OpenGL documentation for help on any 
# drawing functions
#
#
#-----------------------------------------------------------------------------------
# Base objects
#-----------------------------------------------------------------------------------


class OverlayRect():

    ox=10 # origin x
    oy=10 # origin y
    dx=10 # width
    dy=10 # height
    a=1.0 #alpha factor
    
    @classmethod
    def position(self,x,y):
        self.ox=x
        self.oy=y
    
    @classmethod
    def size(self,x,y):
        self.dx=x
        self.dy=y
    
    @classmethod
    def alpha(self,alpha):
        self.a=alpha
    
    @classmethod
    def draw(self):
        bgl.glEnable(bgl.GL_BLEND)
        
        #call subclass draw methods if overwritten
        self.draw_background()
        
        self.on_draw()
                
        # draw borders
        self.draw_border()

        # restore opengl defaults and cleanup
        bgl.glLineWidth(1)
        bgl.glColor4f(0.0, 0.0, 0.0, 1.0)
        bgl.glDisable(bgl.GL_BLEND)
        
        pass
    
    @classmethod 
    def on_draw(self):
        pass
    
    @classmethod 
    def draw_background(self):
        # background 50% alpha, black
        self.on_set_background()
        bgl.glRecti(self.ox, self.oy, self.ox + self.dx, self.oy + self.dy)


    @classmethod 
    def draw_border(self):
        self.on_set_foreground()
        bgl.glLineWidth(2)
        bgl.glBegin(bgl.GL_LINE_LOOP)
        bgl.glVertex2i(self.ox, self.oy)
        bgl.glVertex2i(self.ox, self.oy + self.dy)
        bgl.glVertex2i(self.ox + self.dx, self.oy + self.dy)
        bgl.glVertex2i(self.ox + self.dx, self.oy)     
        bgl.glEnd()

    @classmethod
    def on_set_background(self):
        bgl.glColor4f(0.0, 0.0, 0.0, 0.25*self.a)
        return
    
    @classmethod
    def on_set_foreground(self):
        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)
        return    
        
    @classmethod
    def width(self):
        return self.dx
    
    @classmethod
    def height(self):
        return self.dy
        
    @classmethod
    def left(self):
        return self.ox
    
    @classmethod
    def top(self):
        return self.oy + self.dy
    
    @classmethod
    def right(self):
        return self.ox + self.dx
    
    @classmethod
    def bottom(self):
        return self.oy


#-----------------------------------------------------------------------------------
# OverlayMouse
#-----------------------------------------------------------------------------------

class OverlayMouse(OverlayRect):
    
    #dx = 36 # overides base width
    #dy = 48 # overides base height
    
    bdx=12 # button width
    bdy=12 # button height
    
    lmb=False
    mmb=False
    rmb=False
    
    _scroll=''

    @classmethod
    def size(self,x,y):
        super().size(x,y)
        self.bdx=int(x/3.0)
        self.bdy=int(y/4.0) 
        pass
    
    @classmethod
    def buttons(self,lmb,mmb,rmb):
        self.lmb=lmb
        self.mmb=mmb
        self.rmb=rmb
        
    @classmethod
    def scroll(self,scroll):
        if scroll!='':
            self.buttons(False,False,False)
        self._scroll=scroll
        
    @classmethod
    def on_draw(self):

        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)

        #draw button backgrounds
        if self.lmb == True:
            #bgl.glColor4f(1.0, 0.5, 0.5, 0.5*self.a)
            bgl.glRecti(
                self.left(),
                self.top()-self.bdy,
                self.left() + self.bdx,
                self.top())
            
        if self.mmb == True:
            #bgl.glColor4f(0.5, 0.5, 1.0, 0.5*self.a)
            bgl.glRecti(
                self.ox + self.bdx,
                self.oy + self.dy - self.bdy,
                self.ox + self.dx - self.bdx,
                self.oy + self.dy)
            
        if self.rmb == True:
            #bgl.glColor4f(0.5, 1.0, 0.5, 0.5*self.a)
            bgl.glRecti(
                self.ox + self.dx-self.bdx,
                self.oy + self.dy - self.bdy,
                self.ox + self.dx,
                self.oy + self.dy)
                            
        #draw button dividers
        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)

        if self._scroll!='':
            mx=self.left() + int(self.bdx*1.5)
            my=self.top() - int(self.bdy*0.5)
            dx=4
            dy=0
            #flip
            if self._scroll=='WHEELUPMOUSE':
                dy+=4
            elif self._scroll=='WHEELDOWNMOUSE':
                dy-=4
            #line
            bgl.glLineWidth(3)
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2i(mx, my)
            bgl.glVertex2i(mx, my - dy)
            bgl.glEnd()
            # arrow
            bgl.glLineWidth(1)
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2i(mx - dx, my)
            bgl.glVertex2i(mx, my + dy)
            bgl.glVertex2i(mx + dx, my)
            bgl.glEnd()
                                
        bgl.glLineWidth(1)
        bgl.glBegin(bgl.GL_LINES)
        #left-middle
        bgl.glVertex2i(self.ox+self.bdx, self.oy+self.dy)
        bgl.glVertex2i(self.ox+self.bdx, self.oy+self.dy-self.bdy)
        
        #middle-right
        bgl.glVertex2i(self.ox+self.dx-self.bdx, self.oy+self.dy)
        bgl.glVertex2i(self.ox+self.dx-self.bdx, self.oy+self.dy-self.bdy)
        
        #bottom
        bgl.glVertex2i(self.ox, self.oy+self.dy-self.bdy)
        bgl.glVertex2i(self.ox+self.dx, self.oy+self.dy-self.bdy)   
        
        bgl.glEnd()
        pass


#-----------------------------------------------------------------------------------
# OverlayKey
#-----------------------------------------------------------------------------------
   
class OverlayKey(OverlayRect):
    
    tdx=8 # text offset x
    tdy=8 # text offset y
    font_id = 0 # default font 
    font_size = 20
    _key='Global Key String'
    
    @classmethod
    def __init__(self,key):
        self.key(key) # key text
    
    @classmethod
    def key(self,key):
        self._key=key
        blf.size(self.font_id, self.font_size, 72)
        if key!='':
            dims=blf.dimensions(self.font_id, key)
            dx=int(dims[0])+2*self.tdx
            dy=int(dims[1])+2*self.tdy
            self.size(dx,dy)   
    
    @classmethod
    def draw(self):
        super().draw()
        self.draw_text()
    
    @classmethod
    def draw_text(self):
        #write the text
        self.on_set_text_color()
        blf.position(self.font_id, self.left() + self.tdx, self.bottom() + self.tdy,0)
        blf.size(self.font_id, self.font_size, 72)      
        blf.draw(self.font_id, self._key)

    @classmethod
    def on_set_text_color(self):
        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)


#-----------------------------------------------------------------------------------
# Number Pad
#-----------------------------------------------------------------------------------

class NumpadKey(OverlayKey):
    tdx=3
    tdy=2
    font_size = 10
    borderwidth=1
    
    @classmethod
    def __init__(self,key):
        self._key=key
        self._selected=False

    @classmethod
    def selected(self, select):
        self._selected=select

    @classmethod
    def on_set_text_color(self):
        if self._selected==True:
            bgl.glColor4f(1.0, 1.0, 1.0, self.a)
        else:
            super().on_set_text_color()
    
    @classmethod
    def on_set_background(self):
        #need this to be transparent
        bgl.glColor4f(0.0, 0.0, 0.0, 0.0)
        return
    
    @classmethod
    def on_set_foreground(self):
        if self._selected==True:
            bgl.glColor4f(1.0, 1.0, 1.0, 1.1 * self.a)
        else:
            super().on_set_foreground()
            
    @classmethod
    def draw_border(self):
        if self._selected==False:
            pass
        else:
            super().draw_border()
    

class OverlayNumpad(OverlayRect):
    
    font_id = 0 #default font
    font_size = 12
    _key = ''
    
    @classmethod
    def key(self,key):
        self._key=key
        
    # this is a poor implementation of the draw routine, but having only learned python a week ago
    # this is all I can do to avoid debugging something I have no experience in so keeping it simple ;)
        
    @classmethod
    def draw(self):
        super().draw()
        dy=int(self.height()/5.0)
        dx=int(self.width()/4.0)
        y=self.bottom()
        x=self.left()
        m=-1 #sorry had to hack this as I refactored the code, hence negative int
        
        key0 = NumpadKey('0')
        key0.size(dx*2-m,dy-m)
        key0.position(x,y)
        if self._key=='0':
            key0.selected(True)
        key0.alpha(self.a)
        key0.draw()
        
        keyperiod = NumpadKey('.')
        keyperiod.size(dx-m,dy-m)
        keyperiod.position(x+dx*2,y)
        if self._key=='PERIOD':
            keyperiod.selected(True)
        keyperiod.alpha(self.a)
        keyperiod.draw()
        
        key1 = NumpadKey('1')
        key1.size(dx-m,dy-m)
        key1.position(x,y+dy)
        if self._key=='1':
            key1.selected(True)
        key1.alpha(self.a)
        key1.draw()
        
        key2 = NumpadKey('2')
        key2.size(dx-m,dy-m)
        key2.position(x+dx,y+dy)
        if self._key=='2':
            key2.selected(True)
        key2.alpha(self.a)
        key2.draw()

        key3 = NumpadKey('3')
        key3.size(dx-m,dy-m)
        key3.position(x+dx*2,y+dy)
        if self._key=='3':
            key3.selected(True)
        key3.draw()
        
        #next row
        r=2
        
        key4 = NumpadKey('4')
        key4.size(dx-m,dy-m)
        key4.position(x,y+dy*r)
        if self._key=='4':
            key4.selected(True)
        key4.draw()
        
        key5 = NumpadKey('5')
        key5.size(dx-m,dy-m)
        key5.position(x+dx,y+dy*r)
        if self._key=='5':
            key5.selected(True)
        key5.draw()

        key6 = NumpadKey('6')
        key6.size(dx-m,dy-m)
        key6.position(x+dx*2,y+dy*r)
        if self._key=='6':
            key6.selected(True)
        key6.draw()
             
        #next row
        r=3
        
        key7 = NumpadKey('7')
        key7.size(dx-m,dy-m)
        key7.position(x,y+dy*r)
        if self._key=='7':
            key7.selected(True)
        key7.draw()

        key8 = NumpadKey('8')
        key8.size(dx-m,dy-m)
        key8.position(x+dx,y+dy*r)
        if self._key=='8':
            key8.selected(True)
        key8.draw()

        key9 = NumpadKey('9')
        key9.size(dx-m,dy-m)
        key9.position(x+dx*2,y+dy*r)
        if self._key=='9':
            key9.selected(True)
        key9.draw()
        
        # top row
        r=4
        
        if self._key=='NUM LOCK': #doesn't exist as API event
            pass
        
        # DIVIDE key is named after guitarist from GnR
        
        keydivide = NumpadKey('/')
        keydivide.size(dx-m,dy-m)
        keydivide.position(x+dx,y+dy*r)
        if self._key=='SLASH':
            keydivide.selected(True)
        keydivide.draw()
                
        #quite amusingly the MULPIPLY key has been named after a french cartoon
        keymultiply = NumpadKey('*')
        keymultiply.size(dx-m,dy-m)
        keymultiply.position(x+dx*2,y+dy*r)
        if self._key=='ASTERIX':
            keymultiply.selected(True)
        keymultiply.draw()
        
        keyminus = NumpadKey('-')
        keyminus.size(dx-m,dy-m)
        keyminus.position(x+dx*3,y+dy*r)
        if self._key=='MINUS':
            keyminus.selected(True)
        keyminus.draw()
        
        keyplus = NumpadKey('+')
        keyplus.size(dx-m,dy*2-m)
        keyplus.position(x+dx*3,y+dy*2)
        if self._key=='PLUS':
            keyplus.selected(True)
        keyplus.draw()
        
        #key enter no symbol, so a bit of a hack but zzzzz
        keyenter = NumpadKey('</')
        keyenter.size(dx-m,dy*2-m)
        keyenter.position(x+dx*3,y)
        if self._key=='ENTER':
            keyenter.selected(True)
        keyenter.draw()
        
                   
    @classmethod
    def draw_border(self):
        #call the default
        super().draw_border()

        #innerline
        dy=int(self.height()/5.0)
        dx=int(self.width()/4.0)
        y=self.bottom()
        x=self.left()
        
        bgl.glLineWidth(1)
        bgl.glColor4f(1.0, 1.0, 1.0, 0.25 * self.a)
        bgl.glBegin(bgl.GL_LINES)
        #horizontals
        bgl.glVertex2i(x,y+dy)
        bgl.glVertex2i(x+3*dx,y+dy)
        bgl.glVertex2i(x,y+2*dy)
        bgl.glVertex2i(x+4*dx,y + 2*dy)
        bgl.glVertex2i(x,y+3*dy)
        bgl.glVertex2i(x+3*dx,y + 3*dy)
        bgl.glVertex2i(x,y+4*dy)
        bgl.glVertex2i(x+4*dx,y + 4*dy)
        #verticals
        bgl.glVertex2i(x+dx,y+dy)
        bgl.glVertex2i(x+dx,y + 5*dy)
        bgl.glVertex2i(x+2*dx,y)
        bgl.glVertex2i(x+2*dx,y + 5*dy)
        bgl.glVertex2i(x+3*dx,y)
        bgl.glVertex2i(x+3*dx,y + 5*dy)
        bgl.glEnd()
        pass

#-----------------------------------------------------------------------------------
# Arrows
#-----------------------------------------------------------------------------------
   
class OverlayArrowKey(OverlayRect):

    _key = ''
    
    @classmethod
    def __init__(self,key):
        self.key(key)
    
    @classmethod
    def key(self,key):
        self._key=key

    @classmethod
    def on_draw(self):

        # This function was a lot more compact but a bug in which I thought had
        # been caused by a python scoping error forced me to right this monster
        # The more i use python the less I trust it, but I suppose I'd better
        # give it the benefit of the doubt for now.  I'll revisit this later
        # at least it's clear and functional :(
        
        mx=self.left()+int(0.5*self.width())
        my=self.bottom()+int(0.5*self.height())
        
        r = int(0.25*self.width()) #arrow radius
        
        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)
        bgl.glLineWidth(3)
        
        if self._key == 'UP':     
            bgl.glLineWidth(3)
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2i(mx, my)
            bgl.glVertex2i(mx, my - r)
            bgl.glEnd()
            bgl.glLineWidth(1)
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2i(mx - r, my)
            bgl.glVertex2i(mx, my + r)
            bgl.glVertex2i(mx + r, my)
            bgl.glEnd()
        elif self._key =='DOWN':
            bgl.glLineWidth(3)
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2i(mx, my)
            bgl.glVertex2i(mx, my + r)
            bgl.glEnd()
            bgl.glLineWidth(1)
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2i(mx - r, my)
            bgl.glVertex2i(mx, my - r)
            bgl.glVertex2i(mx + r, my)
            bgl.glEnd()
        elif self._key == 'LEFT':
            bgl.glLineWidth(3)
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2i(mx, my)
            bgl.glVertex2i(mx + r, my)
            bgl.glEnd()
            bgl.glLineWidth(1)
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2i(mx, my + r)
            bgl.glVertex2i(mx - r, my)
            bgl.glVertex2i(mx, my - r)
            bgl.glEnd()
        elif self._key == 'RIGHT':
            bgl.glLineWidth(3)
            bgl.glBegin(bgl.GL_LINES)
            bgl.glVertex2i(mx, my)
            bgl.glVertex2i(mx - r, my)
            bgl.glEnd()
            bgl.glLineWidth(1)
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glVertex2i(mx, my + r)
            bgl.glVertex2i(mx + r,my)
            bgl.glVertex2i(mx, my - r)
            bgl.glEnd()
        else:
           print('Screencast Tutor - Illegal key in OverlayArrow: ' + self._key)
           return


#-----------------------------------------------------------------------------------
# Info Box
#-----------------------------------------------------------------------------------

class OverlayInfo(OverlayRect):
    
    _padding=4 # text padding
    fsize_header=18
    fsize_body=12
    _header='Overlay Help Bar'
    _body='Use this space to display detailed info'
    _body2='Another space to display detailed info'
        
    @classmethod
    def header(self,value):
        self._header=value
        
    @classmethod
    def body(self,value):
        self._body=value

    @classmethod
    def body2(self,value):
        self._body2=value
    
    @classmethod
    def draw(self):
        super().draw()
        self.draw_text()
    
    @classmethod
    def draw_text(self):
        
        font_id = 0 #default font

        bgl.glColor4f(1.0, 1.0, 1.0, 0.5*self.a)

        #write the header text
        offset_x=self._padding
        offset_y=self.fsize_header
        blf.position(font_id, self.left() + offset_x, self.top()-offset_y,0)
        blf.size(font_id, self.fsize_header, 72)
        blf.draw(font_id,self._header)
                
        #write the body text
        offset_x=self._padding + 2        
        offset_y=self.fsize_header + self.fsize_body + self._padding
        blf.position(font_id, self.left() + offset_x, self.top()-offset_y,0)
        blf.size(font_id, self.fsize_body, 72)
        blf.draw(font_id,self._body)

        #write the body2 text
        offset_y=self.fsize_header + self.fsize_body*2 + self._padding
        blf.position(font_id, self.left() + offset_x, self.top()-offset_y,0)
        blf.size(font_id, self.fsize_body, 72)
        blf.draw(font_id,self._body2)


#-----------------------------------------------------------------------------------
# 3D View Drawing Callback
#-----------------------------------------------------------------------------------

def draw_callback_px(self, context):

    if self.ignore==True:
        #print('ignore->' + self.key)
        #return
        pass

    #margins
    mx = 30
    my = 15
    dx = 20

    # cumulative origins
    ox=context.region.width-mx
    oy=context.region.height-my
    
    if self.type in ('MOUSE','SCROLL'):
        mouse = OverlayMouse()
        mouse.size(36,48)
        mouse.position(ox - mouse.width(), oy - mouse.height())
     
        if 'LEFTMOUSE' in self.buttons:
            mouse.buttons(True,False,False)
        if 'MIDDLEMOUSE' in self.buttons:
            mouse.buttons(False,True,False)
        if 'RIGHTMOUSE' in self.buttons:
            mouse.buttons(False,False,True)
        
        mouse.scroll(self.scroll)
        mouse.alpha(self.alpha)
        mouse.draw() 
        
        ox -= mouse.width()
        
    elif self.type in ('KEY'):
        if self.key!='':
            key = OverlayKey(self.key)
            key.position(ox-key.width(), oy-key.height())
            ox-=key.width()
            key.alpha(self.alpha)
            key.draw()  

            # XXX - TODO 'E' key shouldn't be shown in Object Mode
            modded = self.shift or self.ctrl or self.alt
            mode = bpy.context.mode
            help = False
            
            if self.key in ('G','R','S') and mode == 'OBJECT' and not modded:
                help=True
            if self.key in ('G','R','S','E') and mode == 'EDIT_MESH' and not modded:
                help=True
            
            if help==True:
                info=OverlayInfo()
                info.position(mx*2,my*3)
                info.size(context.region.width-mx*3,60)
                info.header('Translation constraints')
                info.body('Press X, Y or Z to constrain to global axis. Twice for local')
                info.body2(' Use shift to lock axis i.e Shift+X constrains to Y and Z axes')
                info.alpha(self.alpha)
                info.draw()
                
        else:
            pass
    elif self.type in ('NUMPAD'):
        if self.key!='':
            pad = OverlayNumpad()
            pad.key(self.key)
            pad.size(48,60)
            pad.position(ox-pad.width(), oy-pad.height())
            ox-=pad.width()
            pad.alpha(self.alpha)
            pad.draw()  
        else:
            pass
    elif self.type in ('ARROW'):
        key = OverlayArrowKey(self.key)
        key.size(31,31)
        key.position(ox-key.width(), oy-key.height())
        ox-=key.width()
        key.alpha(self.alpha)
        key.draw()
    elif self.type in ('SPLASH'):
        splash = OverlayInfo()
        splash.position(mx*2,my*3)
        splash.size(context.region.width-mx*3,60)
        splash.header('ScreenCast Tutor by jiggles100 (NOT FOR COMMERCIAL USE)')
        splash.body('Press F7 to quit.  Thanks to Ton for blender. Olson for testing.')
        splash.alpha(self.alpha)
        splash.draw()
        
    else:
        print("Screencast Tutor ERROR:" + self.type + ":" + self.key) 
 

    if self.shift == True:
        key = OverlayKey('shift')
        ox-= key.width() + dx
        key.position(ox, oy-key.height())
        key.alpha(self.alpha)
        key.draw()
                
    if self.alt == True:
        key = OverlayKey('alt')
        ox-= key.width()+dx
        key.position(ox, oy-key.height())
        key.alpha(self.alpha)
        key.draw()
    
    if self.ctrl == True:
        key = OverlayKey('ctrl')
        ox-= key.width()+dx
        key.position(ox, oy-key.height())
        key.alpha(self.alpha)
        key.draw()
        
    if self.os == True:
        key = OverlayKey('OS')
        ox -= key.width()+dx
        key.position(ox, oy-key.height())
        key.alpha(self.alpha)
        key.draw()


#-----------------------------------------------------------------------------------
# Blender Addon Operator Class Definition
#-----------------------------------------------------------------------------------

class ScreencastTutorOperator(bpy.types.Operator):

    '''F7 to quit'''
    bl_idname = "view3d.screencast_tutor"
    bl_label = "Screencast Tutor"

    def modal(self, context, event):
        
        try:
            context.area.tag_redraw()
        except Exception as ex:
            print(ex)
            return {'RUNNING_MODAL'} 

        if event.type == 'F7': #always listen to quit first
            context.region.callback_remove(self._handle)
            return {'CANCELLED'}
        
        command=event.type
        action=event.value
                                
        # fade alpha regardless of event type
        if self.alpha > 0.0:
            dt = self.timeout - time.clock() + 0.25
            if dt > 0.0:
                self.alpha=(dt/self.delay)**2
            
        # This is not the tidiest parse in the world but this is my first
        # foray into python
        
        # NOTE: event api is inconsistent in naming convention for input
        #       trigger names at this stage. Hopefully this will be
        #       resolved in future 2.6 release
           
        # ignore timer and inbetween and mousemoves and none
        
        if command[:5] in ('TIMER','NONE'):
            self.ignore=True
            return {'PASS_THROUGH'} 
        
        elif command[:9] in ('INBETWEEN','MOUSEMOVE', 'WINDOW_DE'):
            self.ignore=True
            return {'PASS_THROUGH'}
        
        elif command[-5:] in ('SHIFT','_CTRL','T_ALT','OSKEY'):
            self.ignore=True
            return {'PASS_THROUGH'}
        else:
            self.ignore=False

        if action!='RELEASE':
            #reset flags
            self.shift=event.shift
            self.ctrl=event.ctrl
            self.alt=event.alt
            self.os=event.oskey

            
        #reset the alpha and timeout as it's a real event
        self.timeout = time.clock() + self.delay
        self.alpha = 1.0
        
        #scrollwheel
        if command[:5]=='WHEEL':
            self.type='SCROLL'
            self.scroll=command
            return {'PASS_THROUGH'}
        else:
            self.scroll=''
            
        #event tweaks
        if command[:-2]=='EVT_TWEAK':
            #self.type='IGNORE'
            self.tweak=True
            self.buttons=[]
            return {'PASS_THROUGH'}
        else:
            self.tweak=False
            
        #mouse buttons
        if command in ('LEFTMOUSE','MIDDLEMOUSE','RIGHTMOUSE'):
            self.type='MOUSE'
            if action == 'PRESS':
                self.buttons=[command] #.append(event.type)
            elif action == 'RELEASE':
                if command in self.buttons:
                    self.buttons.remove(command)
                else:
                    self.buttons.append(command) #hack for tweak
            elif action == 'CLICK':
                self.buttons.append(command)
            return {'PASS_THROUGH'}
                      
        #arrows
        if command[-5:]=='ARROW':
            self.type='ARROW'
            self.key=command.replace('_ARROW','')
            return {'PASS_THROUGH'}

        #numpad
        elif command[:6]=='NUMPAD':
            self.type='NUMPAD'
            self.key=command.replace('NUMPAD_','')
            return {'PASS_THROUGH'}
                      
        else: #the rest should be regular keys 
            #need to find a way to convert specials              
            self.type='KEY'
            self.key=command.replace('_',' ')
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            
            self.alpha=0.0
            self.delay=1.0
            self.timeout=0.0
            self.ignore=True
            self.type='SPLASH'
            self.key=''
            self.scroll=''
            self.shift=False
            self.ctrl=False
            self.alt=False
            self.os=False
            
            context.window_manager.modal_handler_add(self)

            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = context.region.callback_add(draw_callback_px, (self, context), 'POST_PIXEL')
  

            self.buttons=[]       
            return {'RUNNING_MODAL'}

        else:           
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}

#-----------------------------------------------------------------------------------
# Registration
#-----------------------------------------------------------------------------------

def register():
    bpy.utils.register_class(ScreencastTutorOperator)

def unregister():
    bpy.utils.unregister_class(ScreencastTutorOperator)

if __name__ == "__main__":
    register()
    
    
# whoa that was a tough ride ... a lot of hard work wrestling python, let's just say it's a unique language
# and dleave it at that . Well I'm bushed, I hope you enjoyed the addon
# GB ;)