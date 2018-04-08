@func Foo bool Foo(int a)
  This is a **function** that will take an `int` and return a `bool`. It does
  this through a very fun process.
  @param a int
    This is the random parmeter, it does *things*.
  @param b bool
    This does not exist. But it dosent realy matter.
  @return bool
    This function returns a boolean.

@func Bar int Bar(double a)
  This is a different function, it is called by @ref func:Foo.
  @param a double
    This parameter is converted to an integer.
  @return int
    Returns an `int` representation of the `double` passed to the function.
