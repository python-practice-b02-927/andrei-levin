import graphics as gr

window = gr.GraphWin( "Peyzazh", 700, 700 )

sun = gr.Circle( gr.Point( 500, 200 ), 150 )
sun.setFill('red')

nebo = gr.Rectangle(gr.Point( 0, 0 ), gr.Point( 700, 450 ) )
nebo.setFill('#FF7518')

voda = gr.Rectangle(gr.Point( 0, 700 ), gr.Point( 700, 450 ) )
voda.setFill('#FFA500')

doroga = gr.Rectangle(gr.Point( 450, 450 ), gr.Point( 550, 700 ) )
doroga.setFill('red')

nebo.draw(window)
sun.draw(window)
voda.draw(window)
doroga.draw(window)


window.getMouse()

window.close()
