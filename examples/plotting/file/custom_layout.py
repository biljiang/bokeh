from bokeh.plotting import figure
from bokeh.io import save

template = """
{% block preamble %}
<style>
.plots { display: flex; flex-direction: row; }
.p1, .p2, .p3 { width: 300px; padding: 50px; }
.p1 { background-color: red;   }
.p2 { background-color: green; }
.p3 { background-color: blue;  }
</style>
{% endblock %}
{% block contents %}
<div class="plots">
    <div class="p1">
        {{ embed(roots[0]) }} <!-- or roots.p1 -->
    </div>
    <div class="p2">
        {{ embed(roots[1]) }} <!-- or roots.p2 -->
    </div>
    <div class="p3">
        {{ embed(roots[2]) }} <!-- or roots.p3 -->
    </div>
</div>
{% endblock %}
"""

x = [1, 2, 3]
y = [1, 2, 3]

p1 = figure(name="p1", sizing_mode="scale_width")
p1.scatter(x, y, size=20, fill_color="red")
p2 = figure(name="p2", sizing_mode="scale_width")
p2.scatter(x, y, size=20, fill_color="green")
p3 = figure(name="p3", sizing_mode="scale_width")
p3.scatter(x, y, size=20, fill_color="blue")


save([p1, p2, p3], template=template)
