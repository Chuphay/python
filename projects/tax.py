from google.appengine.ext import ndb
import webapp2


MAIN_PAGE_HTML = """\
<p>here's two boxes, put some floating point numbers (i.e. the number 2.3) in them to represent how much you'd be willing to spend for sector1 or sector2...</p>
  <form action="/compare" method="post">
        <table>
        <tr>
        <td>
      <div><textarea name="content1" rows="3" cols="10"></textarea></div></td>
        <td>
      <div><textarea name="content2" rows="3" cols="10"></textarea></div></td>
      </tr>
      <tr>
      <td>
      <div><input type="submit" value="input"></div></td>
      <td>
      </tr>
      </table>
    </form>
  </body>
</html>
"""

class Data(ndb.Model):
  """Models an individual Data entry with content 1 and 2 and number and date."""
  content1 = ndb.FloatProperty()
  content2 = ndb.FloatProperty()
  number = ndb.IntegerProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write('<html><body>')
        self.response.write(MAIN_PAGE_HTML)
        


class Comparison(webapp2.RequestHandler):

    def post(self):
        """this queries the old data, and then gets the new data, 
        calculates the average, posts that average back to the database,
        so that we can query the average the next time"""
        try:
            old_data = Data.query().order(-Data.date).fetch(1)
            old_var1 = old_data[0].content1
            old_var2 = old_data[0].content2
        except IndexError:
            #this is hopefully only for initialization purposes
            old_var1 = 0.0
            old_var2 = 0.0    
        
        try:
            #try block, in case they don't in a float
            var1 = float(self.request.get('content1'))
            var2 = float(self.request.get('content2'))
            #notice negative numbers are allowed right now
        except ValueError:
            var1 = 0.0
            var2 = 0.0
        try:
            num = old_data[0].number + 1 
        except (TypeError, IndexError):
            #this is hopefully only for initialization purposes
            num = 1
        avg1 = var1/num + old_var1
        avg2 = var2/num +old_var2
                         
        new_data = Data(content1 = avg1, content2 = avg2, number = num)
        new_data.put()
        
        """what you will notice below is a bunch of garbage code, 
        that should be taken care of doing templates... 
        I don't know how to do templates... 
        so that's why we have this garbage code"""
        
        self.response.write('<html><body>Your taxes: <table><tr><td>')
        self.response.write(var1)
        self.response.write('</td><td>')
        self.response.write(var2)
        self.response.write('</td></tr></table>')

        for data in old_data:
            self.response.write('<table><tr><p>What others have said (average)</p><td>')
            self.response.out.write(round(data.content1,2))
            self.response.write('</td><td>')
            self.response.out.write(round(data.content2,2))
            self.response.write('</td><td>')
            
            self.response.write('</td></tr></table><p>place holder for averages (this wont be shown in production)</p>')
            self.response.out.write(data.number)

        self.response.write('</body>')
        self.response.write(MAIN_PAGE_HTML)


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/compare', Comparison),
], debug=True)
