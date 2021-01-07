import psycopg2


# from config import config
def is_user(text):
    lst = text.split()
    print (lst[0])
    print(lst[1])
    sql = """ Select u.u_id,password from  users u
                   WHERE u.u_id = %s and u.password =%s"""
    conn = psycopg2.connect("dbname=project user=postgres password=admin")
    cur = conn.cursor()
    # execute the UPDATE  statement

    ans = cur.execute(sql, (lst[0], lst[1]))
    ans1 = cur.fetchall()
    stri = ans1[0]
    print (stri[0])
    if ans1 is None:
        return 0
    else:
        return stri[0]

def text(id,question):
    """ update vendor name based on the vendor id """
    sql = """Select answer from  qanda q,groupss g,users u WHERE u.u_id =%s and u.group_id =g.g_id and q.g_id=g.id_hi and upper(%s) = upper (q.question)"""
    conn = None

    try:
        # read database configuration

        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=project user=postgres password=admin")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement

        answer = cur.execute(sql, (id, question))
        ans = cur.fetchall()
        if ans is  None:
            return
        else :
            ans1 = ans[0]
    #print (cur.fetchall())
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
       ans1 = ('there is no answer')
    finally:
        if conn is not None:
            conn.close()

    return ans1[0]
