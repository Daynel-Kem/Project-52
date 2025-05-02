import Image from 'next/image'
import React, { useEffect, useRef, useState } from 'react'
import { assets } from '../../../assets/assets'

const Navbar = () => {

  const [isScroll, setIsScroll] = useState(false);
  const sideMenuRef = useRef();

  const openMenu = ()=>{
    sideMenuRef.current.style.transform = 'translateX(-16rem)' 
  }

  const closeMenu = ()=>{
    sideMenuRef.current.style.transform = 'translateX(16rem)' 
  }

  useEffect(()=>{
    window.addEventListener('scroll', ()=>{
      if (scrollY > 50) {
        setIsScroll(true);
      } else {
        setIsScroll(false);
      }
    })
}, [])

  return (
    <div>
    <div className="fixed top-0 right-0 w-11/12 -z-10 translate-y-[-80%]">
      <Image src={assets.header_bg_color} alt="" className="w-full"/>
    </div>

      {/* Make the isScroll be equal to the scroll height or smth and make the the opacity equal to the scroll height so it makes a smooth transition between full navbar and small */}
      <nav className={`z-10 w-full fixed px-5 lg:px-8 xl:px-[8%] py-4 flex items-center justify-between x-50 ${isScroll ? "bg-white/50 backdrop-blur-lg shadow-sm" : ""}`}> 
        <a href="#top">
          <Image src={assets.logo} className='cursor-pointer mr-14 bg-transparent h-17 w-23' alt=""/>
        </a>

        <ul className={`hidden md:flex items-center gap-6 lg:gap-8 rounded-full px-13 py-3 ${isScroll ? "" : "shadow-sm bg-white/50"}`}>
          <li><a className="Ovo" href="#top">Home</a></li>
          <li><a className="Ovo" href="#about">About Me</a></li>
          <li><a className="Ovo" href="#services">Services</a></li>
          <li><a className="Ovo" href="#projects">Projects</a></li>
          <li><a className="Ovo" href="#contact">Contact Me</a></li>
        </ul>

        <div className="flex items-center gap-4">

          <button>
            <Image src={assets.moon_icon} alt="" className="w-6 cursor-pointer"/>
          </button>

          <a href="#contact" className="hidden lg:flex items-center gap-3 px-10 py-2.5 border border-gray-500 bg-white/50 rounded-full ml-4 Ovo">Contact<Image src={assets.arrow_icon} className='w-3' alt="" /></a>

          <button onClick={openMenu} className="block md:hidden ml-3">
            <Image src={assets.menu_black} alt="" className="w-6 cursor-pointer"/>
          </button>
        </div>

        {/* --- mobile menu --- */}

        <ul ref={sideMenuRef} className="flex md:hidden flex-col gap-4 py-20 px-10 fixed -right-64 top-0 bottom-0 w-64 z-50 h-screen bg-rose-50 transition duration-500">
          
          <div className='absolute right-6 top-6' onClick={closeMenu}>
            <Image src={assets.close_black} alt="" className="cursor-pointer w-5"/>
          </div>

          <li><a className="Ovo" onClick={closeMenu} href="#top">Home</a></li>
          <li><a className="Ovo" onClick={closeMenu} href="#about">About Me</a></li>
          <li><a className="Ovo" onClick={closeMenu} href="#services">Services</a></li>
          <li><a className="Ovo" onClick={closeMenu} href="#projects">Projects</a></li>
          <li><a className="Ovo" onClick={closeMenu} href="#contact">Contact Me</a></li>
        </ul>


      </nav>
    </div>
  )
}

export default Navbar
