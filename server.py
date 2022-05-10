import connection

connex_app = connection.connex_app

connex_app.add_api('swagger.yaml')

if __name__ == "__main__":
    connection.db.create_all()
    connex_app.run(debug=True, port=8080)
