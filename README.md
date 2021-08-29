# hi-boy-bsnu-bot

the bot mentions new participants and asks them a set of standard questions

## how-to run

1. clone git repository  
   use: `git clone https://github.com/blackkiv/hi-boy-bsnu-bot.git`
2. in `docker-compose.yml` enter `BOT_TOKEN` environment variable value
3. run `docker-compose`  
   use: `docker-compose up --build -d`
4. you can stop bot with: `docker-compose down --rmi all`  
   it's also delete all downloaded images
