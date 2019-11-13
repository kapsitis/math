package lv.ddgatve.math.build

import java.io.File
import org.apache.commons.io.FileUtils
import org.apache.commons.io.filefilter.TrueFileFilter

import scala.collection.JavaConversions._

object BuildSite {
  
  def copyDirectory(src:String, dest:String): Unit = {
    FileUtils.copyDirectory(new File(src), new File(dest))
  }
   
  def rmDirectory(src:String): Unit = {
    FileUtils.deleteDirectory(new File(src))
  }
  
  
  
  
  def main(args:Array[String]): Unit = {
    //println("HEHE")
    
    val resTypes = List("problembase", "numtheory", "algorithms", "visualizations","rbs") // 'discrete', 'datasearch'
    val skip_directories = List("source-material","static","analysis")

    val osName = System.getProperty("os.name")
    val destRoot = if (osName == "Linux") {
      "../../workspace/linen-tracer-682"
    } else {
       "../../workspace-new/linen-tracer-682"
    }

    for (resType <- resTypes) {
      println(s"$destRoot/$resType-tales")
      val srcRoot = s"src/site/$resType"
      val subDirectories = FileUtils.listFilesAndDirs(new File(srcRoot),
          TrueFileFilter.INSTANCE, TrueFileFilter.INSTANCE)
      
      for (dd <- subDirectories) {
        println(s"Processing with pandoc/reveal, dir=$dd")
      }
    }
    
  }
  
}