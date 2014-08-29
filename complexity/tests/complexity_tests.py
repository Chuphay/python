from nose.tools import *
import complexity.graph as gr


    
u = gr.Vertex('u')
v = gr.Vertex('v')
w = gr.Vertex('w')
e1 = gr.Edge(v, w)
e2 = gr.Edge(u, v)
g = gr.Graph([u,v,w], [e1, e2])

def test_Vertex():
    assert_equal(repr(u), "Vertex('u')")
def test_Edge():
    assert_equal(repr(e1),"Edge(Vertex('v'),Vertex('w'))" )
def test_get():
    assert_equal(g.get_edge(u,w), None)
    assert_equal(str(g.get_edge(v, u)), "Edge(Vertex('u'),Vertex('v'))")
def test_remove():
    g.remove_edge(e1)
    assert_equal(str(g.edges()), "[Edge(Vertex('u'),Vertex('v'))]")
def test_add():
    g.add_edge(e1)
    assert_equal(str(g.edges()), \
          "[Edge(Vertex('u'),Vertex('v')), Edge(Vertex('v'),Vertex('w'))]")
def test_vertices():
    assert_equal(str(g.vertices()), "[Vertex('u'), Vertex('v'), Vertex('w')]")
def test_out():
    assert_equal(str(g.out_vertices(v)),"[Vertex('u'), Vertex('w')]")
    assert_equal(str(g.out_edges(w)), "[Edge(Vertex('v'),Vertex('w'))]")
def test_add_all():
    g.add_all_edges()
    assert_equal(str(g.edges()),\
                 "[Edge(Vertex('u'),Vertex('v')), Edge(Vertex('u'),Vertex('w')), Edge(Vertex('v'),Vertex('w'))]")
    
