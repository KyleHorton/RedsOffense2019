import pymysql
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Author:Kyle Horton
# Project: RedsOffenseDB + Visualization

#establish sql connection
def make_connection():
    return pymysql.connect(
        host='reds-offense.c63ijpxfdwey.us-east-1.rds.amazonaws.com',
        user='admin', 
        password='baseball',
        port=3306,
        autocommit=True)

connect = make_connection()
database = connect.cursor()

database.execute('USE RedsOffense');

def createFigures():
    ## make layout of plotly
    fig = make_subplots(
        rows=3, cols=3,
        specs=[[{"type": "domain"},{"type": "xy", "colspan": 2}, None],
                [{"type": "xy"}, {"type": "domain"}, {"type": "xy"}],
            [{"type": "table", "rowspan": 1, "colspan" : 3}, None, None]], print_grid=True,
        subplot_titles=("2019 Homeruns by Team", "Winker vs Suarez", "Reds Hitters By wRC+", "2019 Stolen Bases by Team", 
                        "HR vs RBI Correlation", "Reds Hitters Roster Info")
    )

    ## league homer query and visualization 
    database.execute("SELECT Team, HR FROM League")
    result = database.fetchall()

    labels = []
    values = []

    for line in result:
        labels.append(line[0])
        values.append(line[1])

    fig.add_trace(
        go.Pie(labels=labels, values=values, showlegend=False, title_font_size=25, hoverinfo='label+percent+value', textinfo='label', textfont_size=10,
                    marker=dict(line=dict(color='#000000', width=2))),
        row=1, col=1
    )
    ## end league homer query and visualization 

    ## Winker vs Suarez query + visualization
    database.execute("""select o.LastName, FLOOR(datediff(curdate(), r.DOB)/365) as 'Age', o.R, o.HR, o.RBI
                        from Outfielders o, Reds r
                        where o.LastName = 'Winker' and r.LastName = 'Winker'
                        UNION
                        Select t.LastName, FLOOR(datediff(curdate(), r.DOB)/365) as 'Age', t.R, t.HR, t.RBI
                        from ThirdBasemen t, Reds r
                        where t.LastName = 'Suarez' and r.LastName = 'Suarez'""")

    result = database.fetchall()
    names = []
    age = []
    runs = []
    hr = []
    rbi = []
    count = 0

    for line in result:
        names.append(line[0])
        age.append(int(line[1]))
        runs.append(line[2])
        hr.append(int(line[3]))
        rbi.append(line[4])

    while (count < 2):  
        fig.add_trace(
            go.Bar(name='', xaxis='x1', hoverinfo="text+y", x=["Age", "Runs", "HR", "RBI"], y=[age[count], runs[count], hr[count], rbi[count]], text=names[count]),
            row=1, col=2
        )
        count +=1


    ## end Winker vs Suarez query + visualization

    ## hitters v wRC query + visualization
    database.execute("""select o.LastName, o.wRC
                    from Outfielders o
                    UNION
                    Select t.LastName, t.wRC
                    from ThirdBasemen t
                    UNION
                    select f.LastName, f.wRC
                    from FirstBasemen f
                    UNION
                    select c.LastName, c.wRC
                    from Catchers c
                    UNION
                    select s.LastName, s.wRC
                    from SecondBasemen s
                    UNION 
                    select ss.LastName, ss.wRC
                    from Shortstops ss;""")

    result = database.fetchall()
    names=[]
    wrc = []
    count = 0

    for line in result:
        names.append(line[0])
        wrc.append(line[1])
        
    while (count < 16):
        fig.add_trace(
        go.Bar(name='', x=[wrc[count]], xaxis='x2',
            y=[names[count]],
            orientation='h'),
            row=2, col=1
        )
        count += 1

    ## end hitters v wRC query + visualization

    ## SB by team query + visualization
    database.execute("Select Team, SB FROM League;")
    result= database.fetchall()

    labels = []
    values = []

    for line in result:
        labels.append(line[0])
        values.append(line[1])

    fig.add_trace(
        go.Pie(name='',labels=labels, values=values, showlegend=False, title_font_size=25, hole=.3, textinfo='label', textfont_size=8),
        row=2, col=2
    )

    ## end SB by team query + visualization

    ## HR v RBI Correlation query + visualization

    database.execute("""select o.LastName, o.HR, o.RBI
                    from Outfielders o
                    UNION
                    Select t.LastName, t.HR, t.RBI
                    from ThirdBasemen t
                    UNION
                    select f.LastName, f.HR, f.RBI
                    from FirstBasemen f
                    UNION
                    select c.LastName, c.HR, c.RBI
                    from Catchers c
                    UNION
                    select s.LastName, s.HR, s.RBI
                    from SecondBasemen s
                    UNION 
                    select ss.LastName, ss.HR, ss.RBI
                    from Shortstops ss;""")
    result= database.fetchall()
    names=[]
    hr = []
    rbi= []

    for line in result:
        names.append(line[0])
        hr.append(int(line[1]))
        rbi.append(int(line[2]))

    fig.add_trace(
        go.Scatter(name="", xaxis='x3',
            x=hr, y=rbi,
            text=names,
            textfont_size=10,
            mode='markers',
            marker_symbol="diamond-cross-open",
            marker_size=10,
        ),
        row=2, col=3
    )
    ## end HR v RBI Correlation query + visualization

    ## roster info query + table ##
    database.execute("SELECT * FROM Reds;")
    result = database.fetchall()
    fname = []
    lname = []
    dob = []
    height = []
    weight = []
    country = []
    position = []

    for line in result:
        fname.append(line[1])
        lname.append(line[2])
        dob.append((line[3]))
        height.append(line[4])
        weight.append(line[5])
        country.append(line[6])
        position.append(line[7])

    ## creates table to display roster info ##
    fig.add_trace(
        go.Table(header=dict(values=['First Name', 'Last Name', 'Date of Birth', 'Height', 'Weight', 'Country', 'Position']),
                    cells=dict(values=[fname, lname, dob, height, weight, country, position]), name="Reds 2019 Hitter Info")
                        ,
        row=3, col=1
    )

    fig.update_layout(autosize=True,height=1650, width=1550, showlegend=False,
                    title={
                        'text': "2019 Reds Hitters Visualization",
                        'y': 0.99,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top',
                        'font_size': 50
                    
    })
    ## end roster info ##
    fig.update_xaxes(title_text="wRC+", row=2, col=1)
    fig.update_xaxes(title_text="Home Runs", row=2, col=3)
    fig.update_yaxes(title_text="Runs Batted In", row=2, col=3)

    #display figures
    fig.show()

createFigures()

#close db
database.close()
connect.close()

