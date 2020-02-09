class ParkingSpot( var ID: (Int, Int) ) {

  var filled = false

  def get(url: String) = scala.io.Source.fromURL(url).mkString

  def checkFilled(): Unit = {
    val parked = get("/scala")
    println(parked)
    if( parked == "true" )
      filled = true
    else
      filled = false
  }

}
