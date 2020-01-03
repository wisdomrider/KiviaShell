set -o emacs;
tab(){
  READLINE_LINE=(compgen -c git)
  READLINE_POINT="${#READLINE_LINE}"
}

bind -x '"\t":"tab"';

for (( ;;)); do
    read -ep " -> " cmd
    python3 func.py $cmd
done


