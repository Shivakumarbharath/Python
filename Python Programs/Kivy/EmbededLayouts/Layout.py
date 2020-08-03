from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class myGridLayout(GridLayout):
    pass


class LayoutApp(App):
    def build(self):
        return myGridLayout()


if __name__ == '__main__':
    LayoutApp().run()
'''
Layout Notes from a Book

There's nothing new in the preceding code, we just implemented the MyGridLayout
class. The final result is shown first in the following screenshot with a few indications
in different colors:
In the preceding screenshot all the types of Kivy layouts are embedded into a
GridLayout of 2 rows by 3 columns. This is a big example, so we are going to study
the corresponding Kivy language code (layouts.kv) in five fragments. Don't be
overwhelmed by the amount of code, it is very straightforward. The following code
is the fragment 1:
105. # File name: layouts.kv (Fragment 1)
106. <MyGridLayout>:
107. rows: 2
108. FloatLayout:
109. Button:
110. text: 'F1'
111. size_hint: .3, .3
GUI Basics – Building an Interface
[ 20 ]
112. pos: 0, 0
113. RelativeLayout:
114. Button:
115. text: 'R1'
116. size_hint: .3, .3
117. pos: 0, 0
In the preceding code, MyGridLayout is first defined by the number of rows
(line 107). Then we add the first two layouts, FloatLayout and RelativeLayout
with one Button each. Both the buttons (F1 and R1) have defined the property
pos: 0,0 (lines 112 and 117) but you can notice in the preceding screenshot
(Embedding Layouts) that the Button F1 (line 110) is in the bottom-left corner of the
whole window, whereas the Button R1 (line 115) is in the bottom-left corner of the
RelativeLayout. The reason for this is that the coordinates in FloatLayout are not
relative to the position of the layout. It is important to mention that this wouldn't have
happened if we have used pos_hint, which always use the relative coordinates.
In the fragment 2, one GridLayout is added to MyGridLayout as shown in the
following code:
118. # File name: layouts.kv (Fragment 2)
119. GridLayout:
120. cols: 2
121. spacing: 10
122. Button:
123. text: 'G1'
124. size_hint_x: None
125. width: 50
126. Button:
127. text: 'G2'
128. Button:
129. text: 'G3'
130. size_hint_x: None
131. width: 50
In the preceding code, we define two columns (line 120) and a spacing of 10 (line
121) which separates the internal widgets by 10 pixels from each other. Also notice
that in the previous screenshot (Embedding Layouts), the first column is thinner than
the second column. We achieved this by setting the size_hint_x property to None
and width to 50 of the buttons G1 (line 122) and G3 (line 128).
Chapter 1
[ 21 ]
In the fragment 3, an AnchorLayout is added as shown in the following code:
132. # File name: layouts.kv (Fragment 3)
133. AnchorLayout:
134. anchor_x: 'right'
135. anchor_y: 'top'
136. Button:
137. text: 'A1'
138. size_hint: [.5, .5]
139. Button:
140. text: 'A2'
141. size_hint: [.2, .2]
In the preceding code, we have specified anchor_x to right and anchor_y to top
(line 134 and 135). You can notice in the previous screenshot (Embedding Layouts)
how both the buttons (lines 136 and 139) of AnchorLayout have been placed in
the top-right corner. This layout is very useful to embed other layouts inside it, for
example top menu bars or side bars.
In the fragment 4, a BoxLayout is added as shown in the following code:
143. # File name: layouts.kv (Fragment 4)
144. BoxLayout:
145. orientation: 'horizontal'
146. Button:
147. text: 'B1'
148. Button:
149. text: 'B2'
150. size_hint: [2, .3]
151. pos_hint: {'y': .4}
152. Button:
153. text: 'B3'
The preceding code illustrates the use of BoxLayout in its horizontal orientation.
Also, in lines 150 and 151 we use size_hint and pos_hint to move the button B2
further up.
Finally, the fragment 5 adds a StackLayout as shown in the following code:
154. # File name: layouts.kv (Fragment 5)
155. StackLayout:
156. orientation: 'rl-tb'
157. padding: 10
158. Button:
159. text: 'S1'
GUI Basics – Building an Interface
[ 22 ]
160. size_hint: [.6, .2]
161. Button:
162. text: 'S2'
163. size_hint: [.4, .4]
164. Button:
165. text: 'S3'
166. size_hint: [.3, .2]
167. Button:
168. text: 'S4'
169. size_hint: [.4, .3]
Here we have added four buttons of different sizes. To understand the rules applied
to organize the widgets in the rl-tb (right-to-left and top-to-bottom) orientation
(line 156) please refer back to the previous screenshot (Embedding Layouts). Also,
you can notice that the padding property (line 157) adds 10 pixels of space between
the widgets and the border of the StackLayout.


'''