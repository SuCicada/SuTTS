
from server import server

if __name__ == '__main__':
    server.main()
    # uvicorn.run("server.server:app", host="0.0.0.0", port=7100,
    #             reload=True, log_level="debug")
