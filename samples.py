import gpt_2_simple as gpt

sess = gpt.start_tf_sess()
gpt.load_gpt2(sess)
# let's hear a random show.
gpt.generate(sess)
# let's hear a random segment
gpt.generate(sess, prefix="this is a segment called")
# let's hear about pc:tng
gpt.generate(sess, prefix="this is a segment called piss constable the next generation")