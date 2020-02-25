package recursive

object Fibonacci {
  def fibonacci(n:Long):Long = {
    n match {
      case 0 => 0
      case 1 => 1
      case n2 => fibonacci(n2-1) + fibonacci(n2-2)
    }
  }
  
  def factorial(n:Int):Int = {
    if (n == 0) return 1
    else return n*factorial(n-1)
  }
  
  
  def main(args: Array[String]): Unit = {
//    println(factorial(10))
    val nn = (1 to 50).toList
    for (n <- nn) {
      val fibN = fibonacci(n) 
      println(s"F($n) = $fibN")
    }
  }
}


