import Image from 'next/image'
import React from 'react'
import { assets } from '../../../assets/assets'
import {motion} from 'motion/react'
import { RotateWords } from './Word-Loop'

const Header = () => {
  return (
    <div className='w-full h-screen flex flex-row justify-center items-center gap-10 z-10' style={{backgroundImage: `url(${assets.bg_image.src})`, backgroundSize: 'cover', backgroundPosition: 'center'}}>
      <motion.div 
      className='flex flex-col items-center sm:items-start text-left w-[50%] mx-[30%] sm:ml-40'
      initial={{opacity:0, x:-100}}
      whileInView={{opacity:1, x:0}}
      transition={{duration: 0.8, type: 'spring', stiffness: 100}}>
        <h3 className="flex flex-col sm:flex-row gap-2 text-xl md:text-2xl mb-3 Ovo items-center sm:items-left text-center sm:text-left">
          Hey, I'm Daniel Kim 
          <motion.div initial={{scale:0}} whileInView={{scale:1}} transition={{duration: 0.8, type: 'spring', stiffness: 100}}>
            <Image src={assets.hand_icon} alt="" className="rounded-full w-6"/>
          </motion.div>
        </h3>
        <div className="flex flex-col sm:width-[80%]">
          <h1 className='text-5xl sm:text-6xl lg:text-[66px] Ovo text-center sm:text-left text-gray-600 sm:text-black '>
              I'm a           
          </h1>
          <RotateWords text="" words={["Student", "Developer", "Friend"]} className='' />
        </div>
        <div className='flex flex-col sm:flex-row items-center gap-4 mt-4'>
          <a href="#contact" className='text-center px-10 py-2 border border-white rounded-full bg-black text-white flex items-center gap-2'>Contact Me <Image src={assets.right_arrow_white} alt="" className="w-4"/></a>
          <a href="/Daniel_Kim_DS_Resume.pdf" download className='px-10 py-2 border rounded-full border-black flex items-center gap-2 bg-white'>My Resume <Image src={assets.download_icon} alt="" className="w-4"/></a>
        </div>
      </motion.div>
      <div className='flex flex-col items-center justify-center w-[50%] mr-0'>
        {/* <Image src={assets.profile_img} alt="" className="rounded-full h-[70%] w-[40%]"/> */}
      </div>
    </div>
  )
}

export default Header
