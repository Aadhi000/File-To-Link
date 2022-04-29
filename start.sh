if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/alone-boy-A/aloneboy-waste.git /aloneboy-waste
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /aloneboy-waste
fi
cd /aloneboy-waste
pip3 install -U -r requirements.txt
echo "Starting File-To-Link..✨✨"
python3 bot.py
